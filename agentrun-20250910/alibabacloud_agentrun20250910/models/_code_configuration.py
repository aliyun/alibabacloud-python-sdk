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
        # The CRC-64 checksum of the code package. If you provide `checksum`, Function Compute verifies that the code package\\"s computed checksum matches this value.
        self.checksum = checksum
        # The command and arguments to run in the runtime.
        self.command = command
        # The programming language for the function\\"s runtime, such as python3 or nodejs.
        self.language = language
        # The name of the OSS bucket that contains the function\\"s code package.
        self.oss_bucket_name = oss_bucket_name
        # The name of the OSS object for the function\\"s code package.
        self.oss_object_name = oss_object_name
        # The base64-encoded content of the agent\\"s code package.
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

