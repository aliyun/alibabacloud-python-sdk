# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListServiceSourceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: List[main_models.ListServiceSourceResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code returned.
        self.code = code
        # The returned data.
        self.data = data
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListServiceSourceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListServiceSourceResponseBodyData(DaraModel):
    def __init__(
        self,
        address: str = None,
        binding_with_gateway: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        group_list: List[str] = None,
        id: int = None,
        ingress_options: main_models.ListServiceSourceResponseBodyDataIngressOptions = None,
        invalid: bool = None,
        name: str = None,
        path_list: List[str] = None,
        source: str = None,
        source_unique_id: str = None,
        type: str = None,
    ):
        # The ID of the Container Service for Kubernetes (ACK) cluster or the endpoint of the Microservices Engine (MSE) instance.
        self.address = address
        # Indicates whether the service source is associated with the gateway. The value 1 indicates that the service source is associated with the gateway.
        self.binding_with_gateway = binding_with_gateway
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The array of service groups.
        self.group_list = group_list
        # The ID.
        self.id = id
        # The information about the support for Ingresses by applications.
        self.ingress_options = ingress_options
        self.invalid = invalid
        # The name.
        self.name = name
        # The array of root paths of service lists.
        self.path_list = path_list
        # The type of the service source.
        self.source = source
        # The unique ID of the service source.
        self.source_unique_id = source_unique_id
        # The type.
        self.type = type

    def validate(self):
        if self.ingress_options:
            self.ingress_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.binding_with_gateway is not None:
            result['BindingWithGateway'] = self.binding_with_gateway

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.group_list is not None:
            result['GroupList'] = self.group_list

        if self.id is not None:
            result['Id'] = self.id

        if self.ingress_options is not None:
            result['IngressOptions'] = self.ingress_options.to_map()

        if self.invalid is not None:
            result['Invalid'] = self.invalid

        if self.name is not None:
            result['Name'] = self.name

        if self.path_list is not None:
            result['PathList'] = self.path_list

        if self.source is not None:
            result['Source'] = self.source

        if self.source_unique_id is not None:
            result['SourceUniqueId'] = self.source_unique_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('BindingWithGateway') is not None:
            self.binding_with_gateway = m.get('BindingWithGateway')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('GroupList') is not None:
            self.group_list = m.get('GroupList')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IngressOptions') is not None:
            temp_model = main_models.ListServiceSourceResponseBodyDataIngressOptions()
            self.ingress_options = temp_model.from_map(m.get('IngressOptions'))

        if m.get('Invalid') is not None:
            self.invalid = m.get('Invalid')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PathList') is not None:
            self.path_list = m.get('PathList')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('SourceUniqueId') is not None:
            self.source_unique_id = m.get('SourceUniqueId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ListServiceSourceResponseBodyDataIngressOptions(DaraModel):
    def __init__(
        self,
        enable_ingress: bool = None,
        enable_status: bool = None,
        ingress_class: str = None,
        watch_namespace: str = None,
    ):
        # Indicates whether Ingresses are enabled.
        self.enable_ingress = enable_ingress
        # Indicates whether the Ingress status is updated.
        self.enable_status = enable_status
        # The Ingress class.
        self.ingress_class = ingress_class
        # The namespace that you want to monitor.
        self.watch_namespace = watch_namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_ingress is not None:
            result['EnableIngress'] = self.enable_ingress

        if self.enable_status is not None:
            result['EnableStatus'] = self.enable_status

        if self.ingress_class is not None:
            result['IngressClass'] = self.ingress_class

        if self.watch_namespace is not None:
            result['WatchNamespace'] = self.watch_namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableIngress') is not None:
            self.enable_ingress = m.get('EnableIngress')

        if m.get('EnableStatus') is not None:
            self.enable_status = m.get('EnableStatus')

        if m.get('IngressClass') is not None:
            self.ingress_class = m.get('IngressClass')

        if m.get('WatchNamespace') is not None:
            self.watch_namespace = m.get('WatchNamespace')

        return self

