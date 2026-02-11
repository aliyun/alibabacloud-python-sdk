# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListProjectLogStoresResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListProjectLogStoresResponseBodyData] = None,
        request_id: str = None,
    ):
        # The data returned.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListProjectLogStoresResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProjectLogStoresResponseBodyData(DaraModel):
    def __init__(
        self,
        end_point: str = None,
        local_name: str = None,
        log_store: str = None,
        main_user_id: int = None,
        project: str = None,
        region_id: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        # The endpoint of the Simple Log Service project.
        self.end_point = end_point
        # The name of the region in which the Simple Log Service project resides.
        self.local_name = local_name
        # The name of the Simple Log Service Logstore.
        self.log_store = log_store
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id
        # The name of the Simple Log Service project.
        self.project = project
        # The ID of the region in which the Simple Log Service project resides.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_id = sub_user_id
        # The username of the Alibaba Cloud account that can be used to perform operations supported by the threat analysis feature.
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.project is not None:
            result['Project'] = self.project

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')

        return self

