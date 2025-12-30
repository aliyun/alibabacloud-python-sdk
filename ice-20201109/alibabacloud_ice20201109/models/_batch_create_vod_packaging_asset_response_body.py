# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class BatchCreateVodPackagingAssetResponseBody(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        request_id: str = None,
        result_list: List[main_models.BatchCreateVodPackagingAssetResponseBodyResultList] = None,
    ):
        # The name of the packaging group.
        self.group_name = group_name
        # The ID of the request.
        self.request_id = request_id
        # The results of asset ingestion.
        self.result_list = result_list

    def validate(self):
        if self.result_list:
            for v1 in self.result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ResultList'] = []
        if self.result_list is not None:
            for k1 in self.result_list:
                result['ResultList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result_list = []
        if m.get('ResultList') is not None:
            for k1 in m.get('ResultList'):
                temp_model = main_models.BatchCreateVodPackagingAssetResponseBodyResultList()
                self.result_list.append(temp_model.from_map(k1))

        return self

class BatchCreateVodPackagingAssetResponseBodyResultList(DaraModel):
    def __init__(
        self,
        asset: main_models.VodPackagingAsset = None,
        code: str = None,
        message: str = None,
    ):
        # The information about the ingested asset.
        self.asset = asset
        # The error code for failed ingestion.
        self.code = code
        # The error message for failed ingestion.
        self.message = message

    def validate(self):
        if self.asset:
            self.asset.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset is not None:
            result['Asset'] = self.asset.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Asset') is not None:
            temp_model = main_models.VodPackagingAsset()
            self.asset = temp_model.from_map(m.get('Asset'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

