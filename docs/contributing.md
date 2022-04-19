# Contributing Guidelines

## 基本排版

- [Material for MkDocs - Reference](https://squidfunk.github.io/mkdocs-material/reference/)

## 多媒体

!!! example "图片"

    === "图片"
        ![](images/avril.png)

    === "Markdown源码"
        ```markdown
        ![](images/avril.png)
        ```

    === "说明"
        ```markdown
        ![](path_to_image)
        ```


!!! example "Youtube视频"

    === "Youtube视频"
        ![type:video](https://www.youtube.com/embed/8xg3vE8Ie_E)

    === "Markdown源码"
        ```markdown
        ![type:video](https://www.youtube.com/embed/8xg3vE8Ie_E)
        ```

    === "说明"
        ```markdown
        ![type:video](https://www.youtube.com/embed/video_id)
        ```

        ![](images/youtube.png)


!!! example "BiliBili视频"

    === "BiliBili视频"
        <iframe src="//player.bilibili.com/player.html?aid=60825989&bvid=BV1kt411A7mK&cid=105846665&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"  style="width: 100%; height: 500px; max-width: 100%；lign:center; padding:20px 0;"> </iframe>

    === "HTML源码"

        ```html
        <iframe src="//player.bilibili.com/player.html?aid=60825989&bvid=BV1kt411A7mK&cid=105846665&page=1"
            scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"
            style="width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;"
        > </iframe>
        ```

    === "说明"

        ![bilibili](images/bilibili.png)

        复制嵌入代码后加上
        ```html
        style="width: 100%; height: 500px; max-width: 100%；align:center; padding:20px 0;"
        ```