from fontTools.ttLib import TTFont
from fontTools.svgLib import svgPath

def ttf_to_svg(ttf_path, output_dir):
    # TTFファイルを読み込む
    font = TTFont(ttf_path)

    # glyfテーブルを取得
    glyf_table = font['glyf']
    cmap = font['cmap'].getBestCmap()

    # グリフをSVG形式で保存
    for glyph_name, glyph in glyf_table.items():
        if glyph.isComposite():
            continue  # コンポジットグリフは無視

        # グリフのパスを取得
        path = glyph.getPath(0, 0)  # x, y 座標を0に設定

        # SVGパス文字列に変換
        svg_path_data = path.toSVG()

        # SVGファイル名を作成
        svg_file_name = f"{output_dir}/{glyph_name}.svg"

        # SVGファイルに保存
        with open(svg_file_name, 'w') as svg_file:
            svg_file.write(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='-100 -100 200 200'>\n")
            svg_file.write(f"<path d='{svg_path_data}' fill='black'/>\n")
            svg_file.write("</svg>")

    print(f"SVG files saved to {output_dir}")

# 使用例
ttf_to_svg("path/to/your/font.ttf", "output/directory")
