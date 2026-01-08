# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSdlStatisticResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sdl_statistic_resp: main_models.DescribeSdlStatisticResponseBodySdlStatisticResp = None,
    ):
        self.request_id = request_id
        self.sdl_statistic_resp = sdl_statistic_resp

    def validate(self):
        if self.sdl_statistic_resp:
            self.sdl_statistic_resp.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sdl_statistic_resp is not None:
            result['SdlStatisticResp'] = self.sdl_statistic_resp.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SdlStatisticResp') is not None:
            temp_model = main_models.DescribeSdlStatisticResponseBodySdlStatisticResp()
            self.sdl_statistic_resp = temp_model.from_map(m.get('SdlStatisticResp'))

        return self

class DescribeSdlStatisticResponseBodySdlStatisticResp(DaraModel):
    def __init__(
        self,
        sdl_asset_top_list: List[main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlAssetTopList] = None,
        sdl_dst_top_list: List[main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlDstTopList] = None,
        sdl_event_type_count_list: List[main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlEventTypeCountList] = None,
    ):
        self.sdl_asset_top_list = sdl_asset_top_list
        self.sdl_dst_top_list = sdl_dst_top_list
        self.sdl_event_type_count_list = sdl_event_type_count_list

    def validate(self):
        if self.sdl_asset_top_list:
            for v1 in self.sdl_asset_top_list:
                 if v1:
                    v1.validate()
        if self.sdl_dst_top_list:
            for v1 in self.sdl_dst_top_list:
                 if v1:
                    v1.validate()
        if self.sdl_event_type_count_list:
            for v1 in self.sdl_event_type_count_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SdlAssetTopList'] = []
        if self.sdl_asset_top_list is not None:
            for k1 in self.sdl_asset_top_list:
                result['SdlAssetTopList'].append(k1.to_map() if k1 else None)

        result['SdlDstTopList'] = []
        if self.sdl_dst_top_list is not None:
            for k1 in self.sdl_dst_top_list:
                result['SdlDstTopList'].append(k1.to_map() if k1 else None)

        result['SdlEventTypeCountList'] = []
        if self.sdl_event_type_count_list is not None:
            for k1 in self.sdl_event_type_count_list:
                result['SdlEventTypeCountList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sdl_asset_top_list = []
        if m.get('SdlAssetTopList') is not None:
            for k1 in m.get('SdlAssetTopList'):
                temp_model = main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlAssetTopList()
                self.sdl_asset_top_list.append(temp_model.from_map(k1))

        self.sdl_dst_top_list = []
        if m.get('SdlDstTopList') is not None:
            for k1 in m.get('SdlDstTopList'):
                temp_model = main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlDstTopList()
                self.sdl_dst_top_list.append(temp_model.from_map(k1))

        self.sdl_event_type_count_list = []
        if m.get('SdlEventTypeCountList') is not None:
            for k1 in m.get('SdlEventTypeCountList'):
                temp_model = main_models.DescribeSdlStatisticResponseBodySdlStatisticRespSdlEventTypeCountList()
                self.sdl_event_type_count_list.append(temp_model.from_map(k1))

        return self

class DescribeSdlStatisticResponseBodySdlStatisticRespSdlEventTypeCountList(DaraModel):
    def __init__(
        self,
        count: str = None,
        event_type: str = None,
    ):
        self.count = count
        self.event_type = event_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.event_type is not None:
            result['EventType'] = self.event_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        return self

class DescribeSdlStatisticResponseBodySdlStatisticRespSdlDstTopList(DaraModel):
    def __init__(
        self,
        public_ip: str = None,
        traffic_bytes: int = None,
    ):
        self.public_ip = public_ip
        self.traffic_bytes = traffic_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.traffic_bytes is not None:
            result['TrafficBytes'] = self.traffic_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('TrafficBytes') is not None:
            self.traffic_bytes = m.get('TrafficBytes')

        return self

class DescribeSdlStatisticResponseBodySdlStatisticRespSdlAssetTopList(DaraModel):
    def __init__(
        self,
        asset_type: str = None,
        public_ip: str = None,
        traffic_bytes: int = None,
    ):
        self.asset_type = asset_type
        self.public_ip = public_ip
        self.traffic_bytes = traffic_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.public_ip is not None:
            result['PublicIp'] = self.public_ip

        if self.traffic_bytes is not None:
            result['TrafficBytes'] = self.traffic_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('PublicIp') is not None:
            self.public_ip = m.get('PublicIp')

        if m.get('TrafficBytes') is not None:
            self.traffic_bytes = m.get('TrafficBytes')

        return self

