import numpy as np
import wave
import sys
from pydub import AudioSegment
from PIL import Image
import os

def read_audio_file(file_path):
    audio = AudioSegment.from_file(file_path)
    audio = audio.set_channels(1)  # モノラルに変換
    audio = audio.set_frame_rate(44100)  # サンプルレートを44100Hzに設定
    audio = audio.apply_gain(-14 - audio.dBFS)  # -14dBにノーマライズ
    samples = np.array(audio.get_array_of_samples())
    samples = samples / (2**15)  # 正規化
    return samples, audio.frame_rate, len(audio)

def calculate_volume(wave_data, framerate, window_ms=10):
    window_size = int(framerate * window_ms / 1000)
    volume = []
    for i in range(0, len(wave_data), window_size):
        window = wave_data[i:i + window_size]
        rms = np.sqrt(np.mean(window**2))
        volume.append(20 * np.log10(rms + 1e-6))  # dBに変換
    return volume

def create_image(processed_volume, output_image_path, total_width=10000, height=100):
    width = len(processed_volume)
    img = Image.new('RGB', (total_width, height), "black")
    pixels = img.load()

    for x in range(total_width):
        normalized_x = int(x * width / total_width)
        color = (255, 255, 255) if processed_volume[normalized_x] == 1 else (0, 0, 0)
        for y in range(height):
            pixels[x, y] = color

    img.save(output_image_path)

def calculate_continuous_periods(processed_volume):
    periods = []
    start = None
    for i, val in enumerate(processed_volume):
        if val == 1 and start is None:
            start = i
        elif val == 0 and start is not None:
            periods.append((start, i - 1))
            start = None
    if start is not None:
        periods.append((start, len(processed_volume) - 1))
    return periods

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python audio-to-graph.py <audio_file>")
        sys.exit(1)

    audio_file = sys.argv[1]
    base_name = os.path.splitext(audio_file)[0]
    output_image_path = f"{base_name}.png"
    output_html_path = f"{base_name}.html"

    wave_data, framerate, audio_length = read_audio_file(audio_file)
    
    volume = calculate_volume(wave_data, framerate)
    processed_volume = [1 if vol > -20 else 0 for vol in volume]
    
    # 連続して1の期間を計算
    continuous_periods = calculate_continuous_periods(processed_volume)
    
    # HTMLファイルに各時間での音量とprocessed_volumeを出力
    with open(output_html_path, 'w') as f:
        f.write("<html><body><table border='1'>")
        f.write("<tr><th>Time (ms)</th><th>Volume (dB)</th><th>Processed Volume</th></tr>")
        for i, (vol, proc_vol) in enumerate(zip(volume, processed_volume)):
            bg_color = "#000000" if proc_vol == 0 else "#FFFFFF"
            text_color = "#FFFFFF" if proc_vol == 0 else "#000000"
            f.write(f"<tr style='background-color:{bg_color}; color:{text_color};'><td>{i * 10}</td><td>{vol:.2f}</td><td>{proc_vol}</td></tr>")
        f.write("</table>")
        
        f.write("<h2>Continuous Periods of 1</h2>")
        f.write("<table border='1'><tr><th>Start (ms)</th><th>End (ms)</th><th>Duration (ms)</th></tr>")
        for start, end in continuous_periods:
            duration = (end - start + 1) * 10
            f.write(f"<tr><td>{start * 10}</td><td>{end * 10}</td><td>{duration}</td></tr>")
        f.write("</table></body></html>")
    
    create_image(processed_volume, output_image_path)
    
    # 入力ファイル名、出力ファイル名、インプットファイルの長さをプリント
    print(f"Input File: {audio_file}")
    print(f"Output Image File: {output_image_path}")
    print(f"Output HTML File: {output_html_path}")
    print(f"Input File Length: {audio_length} ms")