# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_farui20240628 import models as main_models
from darabonba.model import DaraModel

class RunContractExtractRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        fields_to_extract: List[main_models.RunContractExtractRequestFieldsToExtract] = None,
        file_oss_url: str = None,
        region_id: str = None,
    ):
        self.app_id = app_id
        self.fields_to_extract = fields_to_extract
        # This parameter is required.
        self.file_oss_url = file_oss_url
        self.region_id = region_id

    def validate(self):
        if self.fields_to_extract:
            for v1 in self.fields_to_extract:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['appId'] = self.app_id

        result['fieldsToExtract'] = []
        if self.fields_to_extract is not None:
            for k1 in self.fields_to_extract:
                result['fieldsToExtract'].append(k1.to_map() if k1 else None)

        if self.file_oss_url is not None:
            result['fileOssUrl'] = self.file_oss_url

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')

        self.fields_to_extract = []
        if m.get('fieldsToExtract') is not None:
            for k1 in m.get('fieldsToExtract'):
                temp_model = main_models.RunContractExtractRequestFieldsToExtract()
                self.fields_to_extract.append(temp_model.from_map(k1))

        if m.get('fileOssUrl') is not None:
            self.file_oss_url = m.get('fileOssUrl')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

class RunContractExtractRequestFieldsToExtract(DaraModel):
    def __init__(
        self,
        desc: str = None,
        extract_item: str = None,
        option: List[str] = None,
    ):
        self.desc = desc
        self.extract_item = extract_item
        self.option = option

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['desc'] = self.desc

        if self.extract_item is not None:
            result['extractItem'] = self.extract_item

        if self.option is not None:
            result['option'] = self.option

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('extractItem') is not None:
            self.extract_item = m.get('extractItem')

        if m.get('option') is not None:
            self.option = m.get('option')

        return self

