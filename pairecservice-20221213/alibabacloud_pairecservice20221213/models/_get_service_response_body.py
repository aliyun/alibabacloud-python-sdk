# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_pairecservice20221213 import models as main_models
from darabonba.model import DaraModel

class GetServiceResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        engine_config_id: str = None,
        gmt_released_time: str = None,
        image_auth: str = None,
        image_name: str = None,
        latest_prod_release_order: main_models.GetServiceResponseBodyLatestProdReleaseOrder = None,
        name: str = None,
        region: str = None,
        request_id: str = None,
        service_config: str = None,
        service_resource_uri: str = None,
    ):
        self.description = description
        self.engine_config_id = engine_config_id
        self.gmt_released_time = gmt_released_time
        self.image_auth = image_auth
        self.image_name = image_name
        self.latest_prod_release_order = latest_prod_release_order
        self.name = name
        self.region = region
        self.request_id = request_id
        self.service_config = service_config
        self.service_resource_uri = service_resource_uri

    def validate(self):
        if self.latest_prod_release_order:
            self.latest_prod_release_order.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.engine_config_id is not None:
            result['EngineConfigId'] = self.engine_config_id

        if self.gmt_released_time is not None:
            result['GmtReleasedTime'] = self.gmt_released_time

        if self.image_auth is not None:
            result['ImageAuth'] = self.image_auth

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.latest_prod_release_order is not None:
            result['LatestProdReleaseOrder'] = self.latest_prod_release_order.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.service_config is not None:
            result['ServiceConfig'] = self.service_config

        if self.service_resource_uri is not None:
            result['ServiceResourceUri'] = self.service_resource_uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EngineConfigId') is not None:
            self.engine_config_id = m.get('EngineConfigId')

        if m.get('GmtReleasedTime') is not None:
            self.gmt_released_time = m.get('GmtReleasedTime')

        if m.get('ImageAuth') is not None:
            self.image_auth = m.get('ImageAuth')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('LatestProdReleaseOrder') is not None:
            temp_model = main_models.GetServiceResponseBodyLatestProdReleaseOrder()
            self.latest_prod_release_order = temp_model.from_map(m.get('LatestProdReleaseOrder'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ServiceConfig') is not None:
            self.service_config = m.get('ServiceConfig')

        if m.get('ServiceResourceUri') is not None:
            self.service_resource_uri = m.get('ServiceResourceUri')

        return self

class GetServiceResponseBodyLatestProdReleaseOrder(DaraModel):
    def __init__(
        self,
        content: str = None,
        image_version: str = None,
        release_info: str = None,
        release_order_id: str = None,
        releaser: str = None,
        topic: str = None,
    ):
        self.content = content
        self.image_version = image_version
        self.release_info = release_info
        self.release_order_id = release_order_id
        self.releaser = releaser
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.image_version is not None:
            result['ImageVersion'] = self.image_version

        if self.release_info is not None:
            result['ReleaseInfo'] = self.release_info

        if self.release_order_id is not None:
            result['ReleaseOrderId'] = self.release_order_id

        if self.releaser is not None:
            result['Releaser'] = self.releaser

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')

        if m.get('ReleaseInfo') is not None:
            self.release_info = m.get('ReleaseInfo')

        if m.get('ReleaseOrderId') is not None:
            self.release_order_id = m.get('ReleaseOrderId')

        if m.get('Releaser') is not None:
            self.releaser = m.get('Releaser')

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

