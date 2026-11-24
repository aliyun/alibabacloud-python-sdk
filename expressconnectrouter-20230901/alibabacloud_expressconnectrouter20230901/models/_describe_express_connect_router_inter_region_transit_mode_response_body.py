# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_expressconnectrouter20230901 import models as main_models
from darabonba.model import DaraModel

class DescribeExpressConnectRouterInterRegionTransitModeResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        dynamic_code: str = None,
        dynamic_message: str = None,
        http_status_code: int = None,
        inter_region_transit_mode_list: List[main_models.DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # Indicates whether the call was successful. A return value of 200 indicates success, and any other value indicates failure. For the cause of failure, see error codes.
        self.code = code
        # The dynamic error code.
        self.dynamic_code = dynamic_code
        # The dynamic error message, which is used to replace `%s` in the **ErrMessage** response parameter.
        # > If **ErrMessage** returns **The Value of Input Parameter %s is not valid** and **DynamicMessage** returns **DtsJobId**, it indicates that the **DtsJobId** request parameter is invalid.
        self.dynamic_message = dynamic_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The list of cross-region forwarding modes.
        self.inter_region_transit_mode_list = inter_region_transit_mode_list
        # The message returned for the operation.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - **True**: The call was successful.
        # - **False**: The call failed.
        self.success = success

    def validate(self):
        if self.inter_region_transit_mode_list:
            for v1 in self.inter_region_transit_mode_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        if self.code is not None:
            result['Code'] = self.code

        if self.dynamic_code is not None:
            result['DynamicCode'] = self.dynamic_code

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['InterRegionTransitModeList'] = []
        if self.inter_region_transit_mode_list is not None:
            for k1 in self.inter_region_transit_mode_list:
                result['InterRegionTransitModeList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DynamicCode') is not None:
            self.dynamic_code = m.get('DynamicCode')

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.inter_region_transit_mode_list = []
        if m.get('InterRegionTransitModeList') is not None:
            for k1 in m.get('InterRegionTransitModeList'):
                temp_model = main_models.DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList()
                self.inter_region_transit_mode_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeExpressConnectRouterInterRegionTransitModeResponseBodyInterRegionTransitModeList(DaraModel):
    def __init__(
        self,
        mode: str = None,
        region_id: str = None,
    ):
        # The cross-region forwarding mode of the ECR. Valid values:
        # - **ECMP**: load balancing mode.
        # - **NearBy**: nearest forwarding mode.
        self.mode = mode
        # The ID of the region to which the Express Connect Router (ECR) belongs.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

