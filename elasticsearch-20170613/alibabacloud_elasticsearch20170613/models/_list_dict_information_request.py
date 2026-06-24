# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDictInformationRequest(DaraModel):
    def __init__(
        self,
        analyzer_type: str = None,
        bucket_name: str = None,
        key: str = None,
    ):
        # The type of the OSS dictionary to be added. Valid values: IK_HOT, IK, SYNONYMS, and ALIWS. Default value: IK.
        self.analyzer_type = analyzer_type
        # The name of the OSS bucket where the dictionary file is stored.
        # 
        # This parameter is required.
        self.bucket_name = bucket_name
        # The storage path of the dictionary file in the OSS bucket.
        # 
        # This parameter is required.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analyzer_type is not None:
            result['analyzerType'] = self.analyzer_type

        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name

        if self.key is not None:
            result['key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analyzerType') is not None:
            self.analyzer_type = m.get('analyzerType')

        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')

        if m.get('key') is not None:
            self.key = m.get('key')

        return self

