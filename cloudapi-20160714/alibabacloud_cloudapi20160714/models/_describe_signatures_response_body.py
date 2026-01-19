# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeSignaturesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        signature_infos: main_models.DescribeSignaturesResponseBodySignatureInfos = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The returned signature information. It is an array consisting of SignatureInfo data.
        self.signature_infos = signature_infos
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.signature_infos:
            self.signature_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.signature_infos is not None:
            result['SignatureInfos'] = self.signature_infos.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SignatureInfos') is not None:
            temp_model = main_models.DescribeSignaturesResponseBodySignatureInfos()
            self.signature_infos = temp_model.from_map(m.get('SignatureInfos'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSignaturesResponseBodySignatureInfos(DaraModel):
    def __init__(
        self,
        signature_info: List[main_models.DescribeSignaturesResponseBodySignatureInfosSignatureInfo] = None,
    ):
        self.signature_info = signature_info

    def validate(self):
        if self.signature_info:
            for v1 in self.signature_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SignatureInfo'] = []
        if self.signature_info is not None:
            for k1 in self.signature_info:
                result['SignatureInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.signature_info = []
        if m.get('SignatureInfo') is not None:
            for k1 in m.get('SignatureInfo'):
                temp_model = main_models.DescribeSignaturesResponseBodySignatureInfosSignatureInfo()
                self.signature_info.append(temp_model.from_map(k1))

        return self

class DescribeSignaturesResponseBodySignatureInfosSignatureInfo(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        modified_time: str = None,
        region_id: str = None,
        signature_id: str = None,
        signature_key: str = None,
        signature_name: str = None,
        signature_secret: str = None,
    ):
        # The creation time of the key.
        self.created_time = created_time
        # The last modification time of the key.
        self.modified_time = modified_time
        # The region where the key is located.
        self.region_id = region_id
        # The ID of the backend signature key.
        self.signature_id = signature_id
        # The Key value of the backend signature key.
        self.signature_key = signature_key
        # The name of the backend signature key.
        self.signature_name = signature_name
        # The Secret value of the backend signature key.
        self.signature_secret = signature_secret

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.signature_id is not None:
            result['SignatureId'] = self.signature_id

        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key

        if self.signature_name is not None:
            result['SignatureName'] = self.signature_name

        if self.signature_secret is not None:
            result['SignatureSecret'] = self.signature_secret

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SignatureId') is not None:
            self.signature_id = m.get('SignatureId')

        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')

        if m.get('SignatureName') is not None:
            self.signature_name = m.get('SignatureName')

        if m.get('SignatureSecret') is not None:
            self.signature_secret = m.get('SignatureSecret')

        return self

