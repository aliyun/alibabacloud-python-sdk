# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDocParserJobRequest(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        file_url: str = None,
        rag_instance_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        result_type: str = None,
    ):
        self.file_name = file_name
        self.file_url = file_url
        self.rag_instance_id = rag_instance_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.result_type = result_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.rag_instance_id is not None:
            result['RagInstanceId'] = self.rag_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.result_type is not None:
            result['ResultType'] = self.result_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('RagInstanceId') is not None:
            self.rag_instance_id = m.get('RagInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResultType') is not None:
            self.result_type = m.get('ResultType')

        return self

