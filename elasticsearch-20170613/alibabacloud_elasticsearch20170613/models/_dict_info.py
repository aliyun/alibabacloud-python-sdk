# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DictInfo(DaraModel):
    def __init__(
        self,
        file_size: int = None,
        name: str = None,
        source_type: str = None,
        type: str = None,
    ):
        # The size of the dictionary file. Unit: bytes.
        self.file_size = file_size
        # The name of the dictionary file. Requirements:
        # 
        # - Main dictionary or stopword list: one word per line, saved as a UTF-8 encoded DIC file. The file name can contain uppercase and lowercase letters, digits, and underscores, and cannot exceed 30 characters in length. Files with duplicate names are not allowed. The main dictionary file and the stopword file cannot share the same name.
        # - Synonym dictionary: one synonym expression per line, saved as a UTF-8 encoded TXT file.
        # - Alibaba dictionary: the file name must be aliws_ext_dict.txt. The file must be in UTF-8 format. Each line contains one word with no leading or trailing whitespace. Use UNIX or Linux line endings, where each line ends with 
        # . If the file is generated on a Windows system, use the dos2unix tool on a Linux machine to process the dictionary file before uploading it.
        self.name = name
        # The source type of the dictionary file. Valid values:
        # 
        # - OSS: Object Storage Service (OSS). Ensure that the OSS bucket has public-read permission.
        # - ORIGIN: open-source Elasticsearch
        # - UPLOAD: uploaded file.
        self.source_type = source_type
        # The type of the dictionary file. Valid values:
        # 
        # - STOP: stopword list
        # - MAIN: main dictionary
        # - SYNONYMS: synonym dictionary
        # - ALI_WS: Alibaba dictionary.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_size is not None:
            result['fileSize'] = self.file_size

        if self.name is not None:
            result['name'] = self.name

        if self.source_type is not None:
            result['sourceType'] = self.source_type

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileSize') is not None:
            self.file_size = m.get('fileSize')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('sourceType') is not None:
            self.source_type = m.get('sourceType')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

