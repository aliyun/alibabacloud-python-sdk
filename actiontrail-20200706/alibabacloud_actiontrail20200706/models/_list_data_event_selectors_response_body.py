# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_actiontrail20200706 import models as main_models
from darabonba.model import DaraModel

class ListDataEventSelectorsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListDataEventSelectorsResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListDataEventSelectorsResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListDataEventSelectorsResponseBodyData(DaraModel):
    def __init__(
        self,
        data_event_selector_infos: List[main_models.ListDataEventSelectorsResponseBodyDataDataEventSelectorInfos] = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # A list of data event selectors.
        self.data_event_selector_infos = data_event_selector_infos
        # The maximum number of entries returned for the current request.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token

    def validate(self):
        if self.data_event_selector_infos:
            for v1 in self.data_event_selector_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataEventSelectorInfos'] = []
        if self.data_event_selector_infos is not None:
            for k1 in self.data_event_selector_infos:
                result['DataEventSelectorInfos'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_event_selector_infos = []
        if m.get('DataEventSelectorInfos') is not None:
            for k1 in m.get('DataEventSelectorInfos'):
                temp_model = main_models.ListDataEventSelectorsResponseBodyDataDataEventSelectorInfos()
                self.data_event_selector_infos.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

class ListDataEventSelectorsResponseBodyDataDataEventSelectorInfos(DaraModel):
    def __init__(
        self,
        event_selectors: str = None,
        is_trail_all_region: bool = None,
        sls_delivery_configs: List[main_models.ListDataEventSelectorsResponseBodyDataDataEventSelectorInfosSlsDeliveryConfigs] = None,
        trail_arn: str = None,
        trail_name: str = None,
    ):
        # The configuration of the data event selector. This parameter is a JSON array that can contain a maximum of 20 elements.
        # 
        # Each element in the JSON array includes the following fields:
        # 
        # - `ServiceName`: The name of the Alibaba Cloud service that supports data events.
        # 
        # - `ReadWriteType`: The type of data event. Valid values: Read, Write, and All.
        # 
        # - `EventName`: This field contains the `Equals` and `NotEquals` subfields.
        # 
        #   For example, the following configuration specifies that only `GetObject`, `CopyObject`, and `AppendObject`events are delivered:
        # 
        #   `{"EventName":{"Equals":["GetObject","CopyObject","AppendObject"]}}`
        # 
        #   If you specify `NotEquals`, events other than `GetObject`, `CopyObject`, and `AppendObject` are delivered.
        # 
        # - `ResourceArn`: This field also contains the `Equals` and `NotEquals` subfields, similar to `EventName`. For example:
        # 
        #   `{"ResourceArn":{"Equals":[arn1,...,arnx]}}`
        self.event_selectors = event_selectors
        # Specifies whether the trail tracks data events in all regions.
        # 
        # Valid values:
        # 
        # - true
        # 
        # - false
        self.is_trail_all_region = is_trail_all_region
        # The list of configurations for delivering events to Simple Log Service (SLS).
        self.sls_delivery_configs = sls_delivery_configs
        # The ARN of the trail.
        self.trail_arn = trail_arn
        # The name of the trail.
        self.trail_name = trail_name

    def validate(self):
        if self.sls_delivery_configs:
            for v1 in self.sls_delivery_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_selectors is not None:
            result['EventSelectors'] = self.event_selectors

        if self.is_trail_all_region is not None:
            result['IsTrailAllRegion'] = self.is_trail_all_region

        result['SlsDeliveryConfigs'] = []
        if self.sls_delivery_configs is not None:
            for k1 in self.sls_delivery_configs:
                result['SlsDeliveryConfigs'].append(k1.to_map() if k1 else None)

        if self.trail_arn is not None:
            result['TrailArn'] = self.trail_arn

        if self.trail_name is not None:
            result['TrailName'] = self.trail_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSelectors') is not None:
            self.event_selectors = m.get('EventSelectors')

        if m.get('IsTrailAllRegion') is not None:
            self.is_trail_all_region = m.get('IsTrailAllRegion')

        self.sls_delivery_configs = []
        if m.get('SlsDeliveryConfigs') is not None:
            for k1 in m.get('SlsDeliveryConfigs'):
                temp_model = main_models.ListDataEventSelectorsResponseBodyDataDataEventSelectorInfosSlsDeliveryConfigs()
                self.sls_delivery_configs.append(temp_model.from_map(k1))

        if m.get('TrailArn') is not None:
            self.trail_arn = m.get('TrailArn')

        if m.get('TrailName') is not None:
            self.trail_name = m.get('TrailName')

        return self

class ListDataEventSelectorsResponseBodyDataDataEventSelectorInfosSlsDeliveryConfigs(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        error_code: str = None,
        error_message: str = None,
        region_sls_project_arn: str = None,
        status: str = None,
        trail_region: str = None,
    ):
        # The time when the trail was created.
        self.create_time = create_time
        # The error code returned if the resource initialization fails.
        self.error_code = error_code
        # The error message returned if the resource initialization fails.
        self.error_message = error_message
        # The Alibaba Cloud Resource Name (ARN) of the SLS project in the region where events are delivered.
        self.region_sls_project_arn = region_sls_project_arn
        # The initialization status of the tracked resource.
        self.status = status
        # The region of the trail.
        self.trail_region = trail_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.region_sls_project_arn is not None:
            result['RegionSlsProjectArn'] = self.region_sls_project_arn

        if self.status is not None:
            result['Status'] = self.status

        if self.trail_region is not None:
            result['TrailRegion'] = self.trail_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RegionSlsProjectArn') is not None:
            self.region_sls_project_arn = m.get('RegionSlsProjectArn')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrailRegion') is not None:
            self.trail_region = m.get('TrailRegion')

        return self

