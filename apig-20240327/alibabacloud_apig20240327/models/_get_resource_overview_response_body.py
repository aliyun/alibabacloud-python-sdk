# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_apig20240327 import models as main_models
from darabonba.model import DaraModel

class GetResourceOverviewResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetResourceOverviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Response status code.
        self.code = code
        # Resource information.
        self.data = data
        # Response message.
        self.message = message
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetResourceOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetResourceOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        api: main_models.GetResourceOverviewResponseBodyDataApi = None,
        gateway: main_models.GetResourceOverviewResponseBodyDataGateway = None,
        risk_overview: List[main_models.GetResourceOverviewResponseBodyDataRiskOverview] = None,
    ):
        # API information.
        self.api = api
        # Gateway information.
        self.gateway = gateway
        self.risk_overview = risk_overview

    def validate(self):
        if self.api:
            self.api.validate()
        if self.gateway:
            self.gateway.validate()
        if self.risk_overview:
            for v1 in self.risk_overview:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api is not None:
            result['api'] = self.api.to_map()

        if self.gateway is not None:
            result['gateway'] = self.gateway.to_map()

        result['riskOverview'] = []
        if self.risk_overview is not None:
            for k1 in self.risk_overview:
                result['riskOverview'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api') is not None:
            temp_model = main_models.GetResourceOverviewResponseBodyDataApi()
            self.api = temp_model.from_map(m.get('api'))

        if m.get('gateway') is not None:
            temp_model = main_models.GetResourceOverviewResponseBodyDataGateway()
            self.gateway = temp_model.from_map(m.get('gateway'))

        self.risk_overview = []
        if m.get('riskOverview') is not None:
            for k1 in m.get('riskOverview'):
                temp_model = main_models.GetResourceOverviewResponseBodyDataRiskOverview()
                self.risk_overview.append(temp_model.from_map(k1))

        return self

class GetResourceOverviewResponseBodyDataRiskOverview(DaraModel):
    def __init__(
        self,
        count: str = None,
        risk_details: List[main_models.GetResourceOverviewResponseBodyDataRiskOverviewRiskDetails] = None,
        risk_level: str = None,
    ):
        self.count = count
        self.risk_details = risk_details
        self.risk_level = risk_level

    def validate(self):
        if self.risk_details:
            for v1 in self.risk_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        result['riskDetails'] = []
        if self.risk_details is not None:
            for k1 in self.risk_details:
                result['riskDetails'].append(k1.to_map() if k1 else None)

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        self.risk_details = []
        if m.get('riskDetails') is not None:
            for k1 in m.get('riskDetails'):
                temp_model = main_models.GetResourceOverviewResponseBodyDataRiskOverviewRiskDetails()
                self.risk_details.append(temp_model.from_map(k1))

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        return self

class GetResourceOverviewResponseBodyDataRiskOverviewRiskDetails(DaraModel):
    def __init__(
        self,
        gateway_id: str = None,
        gateway_name: str = None,
        risk_level: str = None,
        risk_names: List[str] = None,
        score: str = None,
    ):
        self.gateway_id = gateway_id
        self.gateway_name = gateway_name
        self.risk_level = risk_level
        self.risk_names = risk_names
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway_id is not None:
            result['gatewayId'] = self.gateway_id

        if self.gateway_name is not None:
            result['gatewayName'] = self.gateway_name

        if self.risk_level is not None:
            result['riskLevel'] = self.risk_level

        if self.risk_names is not None:
            result['riskNames'] = self.risk_names

        if self.score is not None:
            result['score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gatewayId') is not None:
            self.gateway_id = m.get('gatewayId')

        if m.get('gatewayName') is not None:
            self.gateway_name = m.get('gatewayName')

        if m.get('riskLevel') is not None:
            self.risk_level = m.get('riskLevel')

        if m.get('riskNames') is not None:
            self.risk_names = m.get('riskNames')

        if m.get('score') is not None:
            self.score = m.get('score')

        return self

class GetResourceOverviewResponseBodyDataGateway(DaraModel):
    def __init__(
        self,
        running_count: int = None,
        total_count: int = None,
    ):
        # Number of running gateways.
        self.running_count = running_count
        # Number of gateway instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.running_count is not None:
            result['runningCount'] = self.running_count

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('runningCount') is not None:
            self.running_count = m.get('runningCount')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class GetResourceOverviewResponseBodyDataApi(DaraModel):
    def __init__(
        self,
        published_count: int = None,
        total_count: int = None,
    ):
        # Number of published APIs.
        self.published_count = published_count
        # Number of APIs.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.published_count is not None:
            result['publishedCount'] = self.published_count

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publishedCount') is not None:
            self.published_count = m.get('publishedCount')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

