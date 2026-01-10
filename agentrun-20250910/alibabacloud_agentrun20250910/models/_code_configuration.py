# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CodeConfiguration(DaraModel):
    def __init__(
        self,
        checksum: str = None,
        command: List[str] = None,
        language: str = None,
        oss_bucket_name: str = None,
        oss_object_name: str = None,
        zip_file: str = None,
    ):
        # 代码包的CRC-64校验值。如果提供了checksum，则函数计算会校验代码包的checksum是否和提供的一致
        self.checksum = checksum
        # 在运行时中运行的命令（例如：[\"python\"]）
        self.command = command
        # 代码运行时的编程语言，如 python3、nodejs 等
        self.language = language
        self.oss_bucket_name = oss_bucket_name
        self.oss_object_name = oss_object_name
        # 智能体代码ZIP包的Base64编码
        self.zip_file = zip_file

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.checksum is not None:
            result['checksum'] = self.checksum

        if self.command is not None:
            result['command'] = self.command

        if self.language is not None:
            result['language'] = self.language

        if self.oss_bucket_name is not None:
            result['ossBucketName'] = self.oss_bucket_name

        if self.oss_object_name is not None:
            result['ossObjectName'] = self.oss_object_name

        if self.zip_file is not None:
            result['zipFile'] = self.zip_file

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('checksum') is not None:
            self.checksum = m.get('checksum')

        if m.get('command') is not None:
            self.command = m.get('command')

        if m.get('language') is not None:
            self.language = m.get('language')

        if m.get('ossBucketName') is not None:
            self.oss_bucket_name = m.get('ossBucketName')

        if m.get('ossObjectName') is not None:
            self.oss_object_name = m.get('ossObjectName')

        if m.get('zipFile') is not None:
            self.zip_file = m.get('zipFile')

        return self

