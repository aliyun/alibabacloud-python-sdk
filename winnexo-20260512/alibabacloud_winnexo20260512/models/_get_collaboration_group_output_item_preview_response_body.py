# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCollaborationGroupOutputItemPreviewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        content: str = None,
        degraded: bool = None,
        download_url: str = None,
        file_ext: str = None,
        file_name: str = None,
        item_id: str = None,
        message: str = None,
        preview_type: str = None,
        preview_url: str = None,
        request_id: str = None,
    ):
        # 公共业务状态码，由后端Code字段映射；错误时用于识别失败原因。
        self.code = code
        # 可直接展示的文本正文或预览提示；不提供正文的文件类型可为空。
        self.content = content
        # 是否降级为下载。true时应展示下载入口，不要按在线文档预览器处理。
        self.degraded = degraded
        # 短期签名下载地址；普通文件有效期3600秒，邮件正文可为空。过期后重新调用本接口。示例仅展示URL格式，不包含真实签名。
        self.download_url = download_url
        # 文件扩展名，不含点；无扩展名时可为空。
        self.file_ext = file_ext
        # 文件名，包含扩展名；无文件名时可为空。
        self.file_name = file_name
        # 对话生成文件的产出明细ID。取GetNodeDetail返回的artifacts中ref.kind为USER_OUTPUT_ITEM的ref.id；不是artifactId。
        self.item_id = item_id
        # 公共错误说明，由后端Message字段映射；错误时描述失败原因。
        self.message = message
        # 预览方式，例如CONTENT为文本正文，HTML为网页，IMAGE为图片，AUDIO为音频，VIDEO为视频，OSS_IMM为文档预览。
        self.preview_type = preview_type
        # 短期预览地址；正文可直接展示时可为空。地址过期后重新调用本接口。示例仅展示URL格式，不是可访问凭证。
        self.preview_url = preview_url
        # 请求追踪ID，由后端RequestId字段映射，用于排查调用失败。
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.content is not None:
            result['content'] = self.content

        if self.degraded is not None:
            result['degraded'] = self.degraded

        if self.download_url is not None:
            result['downloadUrl'] = self.download_url

        if self.file_ext is not None:
            result['fileExt'] = self.file_ext

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.item_id is not None:
            result['itemId'] = self.item_id

        if self.message is not None:
            result['message'] = self.message

        if self.preview_type is not None:
            result['previewType'] = self.preview_type

        if self.preview_url is not None:
            result['previewUrl'] = self.preview_url

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('degraded') is not None:
            self.degraded = m.get('degraded')

        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')

        if m.get('fileExt') is not None:
            self.file_ext = m.get('fileExt')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('itemId') is not None:
            self.item_id = m.get('itemId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('previewType') is not None:
            self.preview_type = m.get('previewType')

        if m.get('previewUrl') is not None:
            self.preview_url = m.get('previewUrl')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

