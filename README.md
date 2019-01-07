# IconMaker

## 介绍

一键生成 Android 所有分辨率 Icon 脚本，支持自定义分辨率（针对 Vivo 等平台对高清分辨率要求）。

## 安装

```
pip install -r requirements.txt
```

## 准备

一张高清 icon 原图，建议 1024x1024，存放至根目录。

## 配置

在 android.json 中进行配置，如无特殊要求，请使用当前配置。

- icon: 原 icon 图片资源
- round: 是否圆角
- round_percent: 圆角百分比，默认 18%
- icon_name: 生成 icon 名称，即 res 目录下名称
- mipmaps: mipmaps 配置
  - name: 一般对应 mipmaps 目录名，如 mipmap-ldpi
  - size: 尺寸，可根据是否高清配置

## 运行

```
python icon_maker.py
```
