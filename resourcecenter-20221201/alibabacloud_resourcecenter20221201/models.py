# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AssociateDefaultFilterRequest(TeaModel):
    def __init__(
        self,
        filter_name: str = None,
    ):
        # The name of the filter.
        # 
        # This parameter is required.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_name is not None:
            result['FilterName'] = self.filter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')
        return self


class AssociateDefaultFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateDefaultFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateDefaultFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateDefaultFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDeliveryChannelRequestDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class CreateDeliveryChannelRequestResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        sls_properties: CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProperties') is not None:
            temp_model = CreateDeliveryChannelRequestResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class CreateDeliveryChannelRequestResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        sls_properties: CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('SlsProperties') is not None:
            temp_model = CreateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: CreateDeliveryChannelRequestDeliveryChannelFilter = None,
        delivery_channel_name: str = None,
        resource_change_delivery: CreateDeliveryChannelRequestResourceChangeDelivery = None,
        resource_snapshot_delivery: CreateDeliveryChannelRequestResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        # This parameter is required.
        self.delivery_channel_filter = delivery_channel_filter
        # This parameter is required.
        self.delivery_channel_name = delivery_channel_name
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = CreateDeliveryChannelRequestDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = CreateDeliveryChannelRequestResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = CreateDeliveryChannelRequestResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class CreateDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFilterRequest(TeaModel):
    def __init__(
        self,
        filter_configuration: str = None,
        filter_name: str = None,
    ):
        # The configurations of the filter.
        # 
        # This parameter is required.
        self.filter_configuration = filter_configuration
        # The name of the filter.
        # 
        # This parameter is required.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_configuration is not None:
            result['FilterConfiguration'] = self.filter_configuration
        if self.filter_name is not None:
            result['FilterName'] = self.filter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConfiguration') is not None:
            self.filter_configuration = m.get('FilterConfiguration')
        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')
        return self


class CreateFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateMultiAccountDeliveryChannelRequestDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        account_scopes: List[str] = None,
        resource_types: List[str] = None,
    ):
        # This parameter is required.
        self.account_scopes = account_scopes
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scopes is not None:
            result['AccountScopes'] = self.account_scopes
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopes') is not None:
            self.account_scopes = m.get('AccountScopes')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class CreateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class CreateMultiAccountDeliveryChannelRequestResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        sls_properties: CreateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProperties') is not None:
            temp_model = CreateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class CreateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        sls_properties: CreateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('SlsProperties') is not None:
            temp_model = CreateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class CreateMultiAccountDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: CreateMultiAccountDeliveryChannelRequestDeliveryChannelFilter = None,
        delivery_channel_name: str = None,
        resource_change_delivery: CreateMultiAccountDeliveryChannelRequestResourceChangeDelivery = None,
        resource_snapshot_delivery: CreateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        # This parameter is required.
        self.delivery_channel_filter = delivery_channel_filter
        # This parameter is required.
        self.delivery_channel_name = delivery_channel_name
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = CreateMultiAccountDeliveryChannelRequestDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = CreateMultiAccountDeliveryChannelRequestResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = CreateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class CreateMultiAccountDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        request_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateMultiAccountDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateMultiAccountDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateMultiAccountDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSavedQueryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
    ):
        # The description of the template.
        # 
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The query statement in the template.
        # 
        # This parameter is required.
        self.expression = expression
        # The name of the template.
        # 
        # *   The name must be 1 to 64 characters in length.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be unique.
        # 
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateSavedQueryResponseBody(TeaModel):
    def __init__(
        self,
        query_id: str = None,
        request_id: str = None,
    ):
        # The template ID.
        self.query_id = query_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateSavedQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSavedQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateSavedQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class DeleteDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFilterRequest(TeaModel):
    def __init__(
        self,
        filter_name: str = None,
    ):
        # The name of the filter.
        # 
        # This parameter is required.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_name is not None:
            result['FilterName'] = self.filter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')
        return self


class DeleteFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMultiAccountDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class DeleteMultiAccountDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteMultiAccountDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMultiAccountDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteMultiAccountDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSavedQueryRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        # The ID of the template.
        # 
        # You can call the [ListSavedQueries](~~ListSavedQueries~~) operation to obtain the template ID.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class DeleteSavedQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteSavedQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSavedQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteSavedQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableMultiAccountResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableMultiAccountResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableMultiAccountResourceCenterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableMultiAccountResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisableResourceCenterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisableResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateDefaultFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateDefaultFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateDefaultFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateDefaultFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableMultiAccountResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The status of the feature. Valid values:
        # 
        # *   Pending: The feature is being enabled.
        # *   Enabled: The feature is enabled.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnableMultiAccountResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableMultiAccountResourceCenterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableMultiAccountResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableResourceCenterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        status: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The activation status of the service. Valid values:
        # 
        # *   Pending: The service is being activated.
        # *   Enabled: The service is activated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class EnableResourceCenterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EnableResourceCenterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableResourceCenterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteMultiAccountSQLQueryRequest(TeaModel):
    def __init__(
        self,
        expression: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
    ):
        # The SQL statement to be executed.
        # 
        # The number of characters in the SQL statement must be less than 2,000.
        # 
        # For more information about the SQL syntax, see [Basic SQL syntax](https://help.aliyun.com/document_detail/2539395.html).
        # 
        # This parameter is required.
        self.expression = expression
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 1000.
        # 
        # Default value: 1000.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The search scope. The value of this parameter can be one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # *   ID of a folder: Resources within all members in the folder are searched.
        # *   ID of a member: Resources within the member are searched.
        # *   ID of a member/ID of a Resource group: Resources within the member in the resource group are searched.
        # 
        # For more information about how to obtain the ID of a resource directory, the Root folder, a folder, a member, or a resource group, see [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html), [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html), [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html), [ListAccounts](https://help.aliyun.com/document_detail/160016.html), or [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html).
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ExecuteMultiAccountSQLQueryResponseBodyColumns(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the column.
        self.name = name
        # The type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ExecuteMultiAccountSQLQueryResponseBody(TeaModel):
    def __init__(
        self,
        columns: List[ExecuteMultiAccountSQLQueryResponseBodyColumns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rows: List[Any] = None,
    ):
        # The columns.
        self.columns = columns
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # An array of search results.
        self.rows = rows

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = ExecuteMultiAccountSQLQueryResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class ExecuteMultiAccountSQLQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteMultiAccountSQLQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteMultiAccountSQLQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSQLQueryRequest(TeaModel):
    def __init__(
        self,
        expression: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
    ):
        # The SQL statement to be executed.
        # 
        # The number of characters in the SQL statement must be less than 2,000.
        # 
        # For more information about the SQL syntax, see [Basic SQL syntax](https://help.aliyun.com/document_detail/2539395.html).
        # 
        # This parameter is required.
        self.expression = expression
        # The number of entries per page.
        # 
        # *   Valid values: 1 to 1000.
        # *   Default value: 1000.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The search scope.
        # 
        # Set this parameter to the ID of a resource group.
        # 
        # For information about how to obtain the ID of a resource group, see [ListResourceGroups](https://help.aliyun.com/document_detail/158855.html).
        self.scope = scope

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ExecuteSQLQueryResponseBodyColumns(TeaModel):
    def __init__(
        self,
        name: str = None,
        type: str = None,
    ):
        # The name of the column.
        self.name = name
        # The type of the column.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ExecuteSQLQueryResponseBody(TeaModel):
    def __init__(
        self,
        columns: List[ExecuteSQLQueryResponseBodyColumns] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        rows: List[Any] = None,
    ):
        # The columns.
        self.columns = columns
        # The number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # An array of search results.
        self.rows = rows

    def validate(self):
        if self.columns:
            for k in self.columns:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Columns'] = []
        if self.columns is not None:
            for k in self.columns:
                result['Columns'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rows is not None:
            result['Rows'] = self.rows
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k in m.get('Columns'):
                temp_model = ExecuteSQLQueryResponseBodyColumns()
                self.columns.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Rows') is not None:
            self.rows = m.get('Rows')
        return self


class ExecuteSQLQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSQLQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteSQLQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetDeliveryChannelResponseBodyDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class GetDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class GetDeliveryChannelResponseBodyResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        sls_properties: GetDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProperties') is not None:
            temp_model = GetDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class GetDeliveryChannelResponseBodyResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        sls_properties: GetDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('SlsProperties') is not None:
            temp_model = GetDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: GetDeliveryChannelResponseBodyDeliveryChannelFilter = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        request_id: str = None,
        resource_change_delivery: GetDeliveryChannelResponseBodyResourceChangeDelivery = None,
        resource_snapshot_delivery: GetDeliveryChannelResponseBodyResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_filter = delivery_channel_filter
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.request_id = request_id
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = GetDeliveryChannelResponseBodyDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = GetDeliveryChannelResponseBodyResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = GetDeliveryChannelResponseBodyResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class GetDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeliveryChannelStatisticsRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        latest_change_delivery_time: str = None,
        latest_snapshot_delivery_time: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.latest_change_delivery_time = latest_change_delivery_time
        self.latest_snapshot_delivery_time = latest_snapshot_delivery_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.latest_change_delivery_time is not None:
            result['LatestChangeDeliveryTime'] = self.latest_change_delivery_time
        if self.latest_snapshot_delivery_time is not None:
            result['LatestSnapshotDeliveryTime'] = self.latest_snapshot_delivery_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('LatestChangeDeliveryTime') is not None:
            self.latest_change_delivery_time = m.get('LatestChangeDeliveryTime')
        if m.get('LatestSnapshotDeliveryTime') is not None:
            self.latest_snapshot_delivery_time = m.get('LatestSnapshotDeliveryTime')
        return self


class GetDeliveryChannelStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_statistics: GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics = None,
        request_id: str = None,
    ):
        self.delivery_channel_statistics = delivery_channel_statistics
        self.request_id = request_id

    def validate(self):
        if self.delivery_channel_statistics:
            self.delivery_channel_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_statistics is not None:
            result['DeliveryChannelStatistics'] = self.delivery_channel_statistics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelStatistics') is not None:
            temp_model = GetDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics()
            self.delivery_channel_statistics = temp_model.from_map(m['DeliveryChannelStatistics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetDeliveryChannelStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeliveryChannelStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetDeliveryChannelStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExampleQueryRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        # The ID of the template.
        # 
        # >  You can call the [ListExampleQueries](~~ListExampleQueries~~) operation to obtain the template ID.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class GetExampleQueryResponseBodyExampleQuery(TeaModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        self.description = description
        # The query statement in the template.
        self.expression = expression
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.name is not None:
            result['Name'] = self.name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class GetExampleQueryResponseBody(TeaModel):
    def __init__(
        self,
        example_query: GetExampleQueryResponseBodyExampleQuery = None,
        request_id: str = None,
    ):
        # The information about the sample query template.
        self.example_query = example_query
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.example_query:
            self.example_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.example_query is not None:
            result['ExampleQuery'] = self.example_query.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExampleQuery') is not None:
            temp_model = GetExampleQueryResponseBodyExampleQuery()
            self.example_query = temp_model.from_map(m['ExampleQuery'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetExampleQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExampleQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExampleQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        account_scopes: List[str] = None,
        resource_types: List[str] = None,
    ):
        self.account_scopes = account_scopes
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scopes is not None:
            result['AccountScopes'] = self.account_scopes
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopes') is not None:
            self.account_scopes = m.get('AccountScopes')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        sls_properties: GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SlsProperties') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBodyResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        sls_properties: GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('SlsProperties') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class GetMultiAccountDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        request_id: str = None,
        resource_change_delivery: GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery = None,
        resource_snapshot_delivery: GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_filter = delivery_channel_filter
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.request_id = request_id
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBodyDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBodyResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBodyResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class GetMultiAccountDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMultiAccountDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountDeliveryChannelStatisticsRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
    ):
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        return self


class GetMultiAccountDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics(TeaModel):
    def __init__(
        self,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        latest_change_delivery_time: str = None,
        latest_snapshot_delivery_time: str = None,
    ):
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.latest_change_delivery_time = latest_change_delivery_time
        self.latest_snapshot_delivery_time = latest_snapshot_delivery_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.latest_change_delivery_time is not None:
            result['LatestChangeDeliveryTime'] = self.latest_change_delivery_time
        if self.latest_snapshot_delivery_time is not None:
            result['LatestSnapshotDeliveryTime'] = self.latest_snapshot_delivery_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('LatestChangeDeliveryTime') is not None:
            self.latest_change_delivery_time = m.get('LatestChangeDeliveryTime')
        if m.get('LatestSnapshotDeliveryTime') is not None:
            self.latest_snapshot_delivery_time = m.get('LatestSnapshotDeliveryTime')
        return self


class GetMultiAccountDeliveryChannelStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channel_statistics: GetMultiAccountDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics = None,
        request_id: str = None,
    ):
        self.delivery_channel_statistics = delivery_channel_statistics
        self.request_id = request_id

    def validate(self):
        if self.delivery_channel_statistics:
            self.delivery_channel_statistics.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_statistics is not None:
            result['DeliveryChannelStatistics'] = self.delivery_channel_statistics.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelStatistics') is not None:
            temp_model = GetMultiAccountDeliveryChannelStatisticsResponseBodyDeliveryChannelStatistics()
            self.delivery_channel_statistics = temp_model.from_map(m['DeliveryChannelStatistics'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetMultiAccountDeliveryChannelStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountDeliveryChannelStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMultiAccountDeliveryChannelStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountResourceCenterServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        initial_status: str = None,
        request_id: str = None,
        service_status: str = None,
    ):
        # The initialization status of the feature. Valid values:
        # 
        # *   Pending: The feature is being initialized.
        # *   Finished: The feature is initialized.
        self.initial_status = initial_status
        # The ID of the request.
        self.request_id = request_id
        # The status of the feature. Valid values:
        # 
        # *   Enabled: The feature is enabled.
        # *   Disabled: The feature is disabled.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_status is not None:
            result['InitialStatus'] = self.initial_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialStatus') is not None:
            self.initial_status = m.get('InitialStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetMultiAccountResourceCenterServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountResourceCenterServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMultiAccountResourceCenterServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMultiAccountResourceConfigurationRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The type of the resource.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetMultiAccountResourceConfigurationResponseBodyIpAddressAttributes(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip_address = ip_address
        # The network type. Valid values:
        # 
        # *   **Public**: the Internet
        # *   **Private**: internal network
        self.network_type = network_type
        # The version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetMultiAccountResourceConfigurationResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetMultiAccountResourceConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[GetMultiAccountResourceConfigurationResponseBodyIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[GetMultiAccountResourceConfigurationResponseBodyTags] = None,
        zone_id: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The configurations of the resource.
        self.configuration = configuration
        # The time when the resource was created.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The attributes of the IP address.
        self.ip_address_attributes = ip_address_attributes
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        self.zone_id = zone_id

    def validate(self):
        if self.ip_address_attributes:
            for k in self.ip_address_attributes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        result['IpAddressAttributes'] = []
        if self.ip_address_attributes is not None:
            for k in self.ip_address_attributes:
                result['IpAddressAttributes'].append(k.to_map() if k else None)
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        self.ip_address_attributes = []
        if m.get('IpAddressAttributes') is not None:
            for k in m.get('IpAddressAttributes'):
                temp_model = GetMultiAccountResourceConfigurationResponseBodyIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k))
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetMultiAccountResourceConfigurationResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetMultiAccountResourceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMultiAccountResourceConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetMultiAccountResourceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceCenterServiceStatusResponseBody(TeaModel):
    def __init__(
        self,
        initial_status: str = None,
        request_id: str = None,
        service_status: str = None,
    ):
        # The initialization status of the service. Valid values:
        # 
        # *   Pending: The service is being initialized.
        # *   Finished: The service is initialized.
        self.initial_status = initial_status
        # The ID of the request.
        self.request_id = request_id
        # The status of the service. Valid values:
        # 
        # *   Enabled: The service is activated.
        # *   Disabled: The service is deactivated.
        self.service_status = service_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.initial_status is not None:
            result['InitialStatus'] = self.initial_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.service_status is not None:
            result['ServiceStatus'] = self.service_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InitialStatus') is not None:
            self.initial_status = m.get('InitialStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ServiceStatus') is not None:
            self.service_status = m.get('ServiceStatus')
        return self


class GetResourceCenterServiceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceCenterServiceStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceCenterServiceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceConfigurationRequest(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_region_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.resource_region_id = resource_region_id
        # The type of the resource.
        # 
        # For more information about the resource types supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class GetResourceConfigurationResponseBodyIpAddressAttributes(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip_address = ip_address
        # The network type. Valid values:
        # 
        # *   **Public**: the Internet
        # *   **Private**: internal network
        self.network_type = network_type
        # The version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetResourceConfigurationResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetResourceConfigurationResponseBody(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        configuration: Dict[str, Any] = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[GetResourceConfigurationResponseBodyIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[GetResourceConfigurationResponseBodyTags] = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.account_id = account_id
        # The configurations of the resource.
        self.configuration = configuration
        # The time when the resource was created.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The attributes of the IP address.
        self.ip_address_attributes = ip_address_attributes
        # The IP addresses.
        # 
        # > Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the resource belongs.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        self.resource_id = resource_id
        # The name of the resource.
        self.resource_name = resource_name
        # The type of the resource.
        self.resource_type = resource_type
        # The tags of the resource.
        self.tags = tags
        # The zone ID of the resource.
        self.zone_id = zone_id

    def validate(self):
        if self.ip_address_attributes:
            for k in self.ip_address_attributes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.configuration is not None:
            result['Configuration'] = self.configuration
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        result['IpAddressAttributes'] = []
        if self.ip_address_attributes is not None:
            for k in self.ip_address_attributes:
                result['IpAddressAttributes'].append(k.to_map() if k else None)
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('Configuration') is not None:
            self.configuration = m.get('Configuration')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        self.ip_address_attributes = []
        if m.get('IpAddressAttributes') is not None:
            for k in m.get('IpAddressAttributes'):
                temp_model = GetResourceConfigurationResponseBodyIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k))
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetResourceConfigurationResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class GetResourceConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceConfigurationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceConfigurationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceCountsRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetResourceCountsRequest(TeaModel):
    def __init__(
        self,
        filter: List[GetResourceCountsRequestFilter] = None,
        group_by_key: str = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The dimension by which resources are queried. Valid values:
        # 
        # *   ResourceType
        # *   Region
        # *   ResourceGroupId
        # *   TagKey
        # *   TagValue
        self.group_by_key = group_by_key

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = GetResourceCountsRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        return self


class GetResourceCountsResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class GetResourceCountsResponseBodyResourceCounts(TeaModel):
    def __init__(
        self,
        count: int = None,
        group_name: str = None,
    ):
        # The number of resources.
        self.count = count
        # The group name.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.group_name is not None:
            result['GroupName'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')
        return self


class GetResourceCountsResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[GetResourceCountsResponseBodyFilters] = None,
        group_by_key: str = None,
        request_id: str = None,
        resource_counts: List[GetResourceCountsResponseBodyResourceCounts] = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The dimension by which resources are queried.
        self.group_by_key = group_by_key
        # The request ID.
        self.request_id = request_id
        # The numbers of resources.
        self.resource_counts = resource_counts

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resource_counts:
            for k in self.resource_counts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.group_by_key is not None:
            result['GroupByKey'] = self.group_by_key
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceCounts'] = []
        if self.resource_counts is not None:
            for k in self.resource_counts:
                result['ResourceCounts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = GetResourceCountsResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('GroupByKey') is not None:
            self.group_by_key = m.get('GroupByKey')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_counts = []
        if m.get('ResourceCounts') is not None:
            for k in m.get('ResourceCounts'):
                temp_model = GetResourceCountsResponseBodyResourceCounts()
                self.resource_counts.append(temp_model.from_map(k))
        return self


class GetResourceCountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceCountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceCountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSavedQueryRequest(TeaModel):
    def __init__(
        self,
        query_id: str = None,
    ):
        # The template ID.
        # 
        # >  You can call the [ListSavedQueries](~~ListSavedQueries~~) operation to query the ID.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class GetSavedQueryResponseBodySavedQuery(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
        update_time: str = None,
    ):
        # The time when the template was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the template.
        self.description = description
        # The query statement in the template.
        self.expression = expression
        # The name of the template.
        self.name = name
        # The template ID.
        self.query_id = query_id
        # The time when the template was updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.name is not None:
            result['Name'] = self.name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetSavedQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        saved_query: GetSavedQueryResponseBodySavedQuery = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The information about the template.
        self.saved_query = saved_query

    def validate(self):
        if self.saved_query:
            self.saved_query.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.saved_query is not None:
            result['SavedQuery'] = self.saved_query.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SavedQuery') is not None:
            temp_model = GetSavedQueryResponseBodySavedQuery()
            self.saved_query = temp_model.from_map(m['SavedQuery'])
        return self


class GetSavedQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSavedQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetSavedQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeliveryChannelsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListDeliveryChannelsResponseBodyDeliveryChannels(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        delivery_channel_description: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
    ):
        self.create_time = create_time
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        return self


class ListDeliveryChannelsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channels: List[ListDeliveryChannelsResponseBodyDeliveryChannels] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k in m.get('DeliveryChannels'):
                temp_model = ListDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListDeliveryChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeliveryChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListDeliveryChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExampleQueriesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 50.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListExampleQueriesResponseBodyExampleQueries(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        self.description = description
        # The name of the template.
        self.name = name
        # The ID of the template.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class ListExampleQueriesResponseBody(TeaModel):
    def __init__(
        self,
        example_queries: List[ListExampleQueriesResponseBodyExampleQueries] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The information about the sample query templates.
        self.example_queries = example_queries
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.example_queries:
            for k in self.example_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ExampleQueries'] = []
        if self.example_queries is not None:
            for k in self.example_queries:
                result['ExampleQueries'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.example_queries = []
        if m.get('ExampleQueries') is not None:
            for k in m.get('ExampleQueries'):
                temp_model = ListExampleQueriesResponseBodyExampleQueries()
                self.example_queries.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListExampleQueriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExampleQueriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExampleQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFiltersResponseBodyFilters(TeaModel):
    def __init__(
        self,
        filter_configuration: str = None,
        filter_name: str = None,
    ):
        # The configurations of the filter.
        # 
        # This parameter is required.
        self.filter_configuration = filter_configuration
        # The name of the filter.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_configuration is not None:
            result['FilterConfiguration'] = self.filter_configuration
        if self.filter_name is not None:
            result['FilterName'] = self.filter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConfiguration') is not None:
            self.filter_configuration = m.get('FilterConfiguration')
        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')
        return self


class ListFiltersResponseBody(TeaModel):
    def __init__(
        self,
        default_filter_name: str = None,
        filters: List[ListFiltersResponseBodyFilters] = None,
        request_id: str = None,
    ):
        # The name of the default filter.
        self.default_filter_name = default_filter_name
        # The configurations of the filter.
        self.filters = filters
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_filter_name is not None:
            result['DefaultFilterName'] = self.default_filter_name
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultFilterName') is not None:
            self.default_filter_name = m.get('DefaultFilterName')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListFiltersResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListFiltersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFiltersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListFiltersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountDeliveryChannelsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListMultiAccountDeliveryChannelsResponseBodyDeliveryChannels(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        delivery_channel_description: str = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
    ):
        self.create_time = create_time
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        return self


class ListMultiAccountDeliveryChannelsResponseBody(TeaModel):
    def __init__(
        self,
        delivery_channels: List[ListMultiAccountDeliveryChannelsResponseBodyDeliveryChannels] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.delivery_channels = delivery_channels
        self.max_results = max_results
        # This parameter is required.
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.delivery_channels:
            for k in self.delivery_channels:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeliveryChannels'] = []
        if self.delivery_channels is not None:
            for k in self.delivery_channels:
                result['DeliveryChannels'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.delivery_channels = []
        if m.get('DeliveryChannels') is not None:
            for k in m.get('DeliveryChannels'):
                temp_model = ListMultiAccountDeliveryChannelsResponseBodyDeliveryChannels()
                self.delivery_channels.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListMultiAccountDeliveryChannelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountDeliveryChannelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMultiAccountDeliveryChannelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_ids: List[str] = None,
    ):
        # The ID of the management account or member of the resource directory.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The maximum number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 10.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The IDs of resource groups.
        self.resource_group_ids = resource_group_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_ids is not None:
            result['ResourceGroupIds'] = self.resource_group_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupIds') is not None:
            self.resource_group_ids = m.get('ResourceGroupIds')
        return self


class ListMultiAccountResourceGroupsResponseBodyResourceGroups(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_date: str = None,
        display_name: str = None,
        id: str = None,
        name: str = None,
        status: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The time when the resource group was created.
        self.create_date = create_date
        # The display name of the resource group.
        self.display_name = display_name
        # The ID of the resource group.
        self.id = id
        # The unique identifier of the resource group.
        self.name = name
        # The status of the resource group. Valid values:
        # 
        # *   Creating: The resource group is being created.
        # *   OK: The resource group is created.
        # *   PendingDelete: The resource group is waiting to be deleted.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_date is not None:
            result['CreateDate'] = self.create_date
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateDate') is not None:
            self.create_date = m.get('CreateDate')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListMultiAccountResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        resource_groups: List[ListMultiAccountResourceGroupsResponseBodyResourceGroups] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resource groups.
        self.resource_groups = resource_groups

    def validate(self):
        if self.resource_groups:
            for k in self.resource_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceGroups'] = []
        if self.resource_groups is not None:
            for k in self.resource_groups:
                result['ResourceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_groups = []
        if m.get('ResourceGroups') is not None:
            for k in m.get('ResourceGroups'):
                temp_model = ListMultiAccountResourceGroupsResponseBodyResourceGroups()
                self.resource_groups.append(temp_model.from_map(k))
        return self


class ListMultiAccountResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountResourceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMultiAccountResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching method.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListMultiAccountResourceRelationshipsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        related_resource_filter: List[ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter] = None,
        resource_id: str = None,
        resource_type: str = None,
        scope: str = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The filter conditions for resources associated with the resource.
        self.related_resource_filter = related_resource_filter
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The search scope. Valid values:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to query the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to query the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to query the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](https://help.aliyun.com/document_detail/160016.html) operation to query the ID.
        # 
        # This parameter is required.
        self.scope = scope

    def validate(self):
        if self.related_resource_filter:
            for k in self.related_resource_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RelatedResourceFilter'] = []
        if self.related_resource_filter is not None:
            for k in self.related_resource_filter:
                result['RelatedResourceFilter'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.related_resource_filter = []
        if m.get('RelatedResourceFilter') is not None:
            for k in m.get('RelatedResourceFilter'):
                temp_model = ListMultiAccountResourceRelationshipsRequestRelatedResourceFilter()
                self.related_resource_filter.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ListMultiAccountResourceRelationshipsResponseBodyResourceRelationships(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        region_id: str = None,
        related_resource_id: str = None,
        related_resource_region_id: str = None,
        related_resource_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The ID of the management account or member.
        self.account_id = account_id
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the associated resource.
        self.related_resource_id = related_resource_id
        # The region ID of the associated resource.
        self.related_resource_region_id = related_resource_region_id
        # The type of the associated resource.
        self.related_resource_type = related_resource_type
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_resource_id is not None:
            result['RelatedResourceId'] = self.related_resource_id
        if self.related_resource_region_id is not None:
            result['RelatedResourceRegionId'] = self.related_resource_region_id
        if self.related_resource_type is not None:
            result['RelatedResourceType'] = self.related_resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedResourceId') is not None:
            self.related_resource_id = m.get('RelatedResourceId')
        if m.get('RelatedResourceRegionId') is not None:
            self.related_resource_region_id = m.get('RelatedResourceRegionId')
        if m.get('RelatedResourceType') is not None:
            self.related_resource_type = m.get('RelatedResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListMultiAccountResourceRelationshipsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_relationships: List[ListMultiAccountResourceRelationshipsResponseBodyResourceRelationships] = None,
        scope: str = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resource relationships.
        self.resource_relationships = resource_relationships
        # The search scope. Valid values:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # *   ID of a folder: Resources within all members in the folder are searched.
        # *   ID of a member: Resources within the member are searched.
        self.scope = scope

    def validate(self):
        if self.resource_relationships:
            for k in self.resource_relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceRelationships'] = []
        if self.resource_relationships is not None:
            for k in self.resource_relationships:
                result['ResourceRelationships'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_relationships = []
        if m.get('ResourceRelationships') is not None:
            for k in m.get('ResourceRelationships'):
                temp_model = ListMultiAccountResourceRelationshipsResponseBodyResourceRelationships()
                self.resource_relationships.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class ListMultiAccountResourceRelationshipsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountResourceRelationshipsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMultiAccountResourceRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountTagKeysRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        tag_key: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The search scope. The value of this parameter can be one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID of the resource directory. The ID is indicated by the `ResourceDirectoryId` parameter in the response of the operation.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID of the Root folder. The ID is indicated by the `RootFolderId` parameter in the response of the operation.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID of the folder. The ID is indicated by the `FolderId` parameter in the response of the operation.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](https://help.aliyun.com/document_detail/160016.html) operation to obtain the ID of the member. The ID is indicated by the `AccountId` parameter in the response of the operation.
        # 
        # This parameter is required.
        self.scope = scope
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListMultiAccountTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class ListMultiAccountTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMultiAccountTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMultiAccountTagValuesRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The search scope. You can set the value to one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](https://help.aliyun.com/document_detail/160016.html) operation to obtain the ID.
        self.scope = scope
        # The tag key.
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListMultiAccountTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class ListMultiAccountTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMultiAccountTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListMultiAccountTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceRelationshipsRequestRelatedResourceFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching method.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListResourceRelationshipsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        region_id: str = None,
        related_resource_filter: List[ListResourceRelationshipsRequestRelatedResourceFilter] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 500.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the resource.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The filter conditions for resources associated with the resource.
        self.related_resource_filter = related_resource_filter
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource.
        # 
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        if self.related_resource_filter:
            for k in self.related_resource_filter:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        result['RelatedResourceFilter'] = []
        if self.related_resource_filter is not None:
            for k in self.related_resource_filter:
                result['RelatedResourceFilter'].append(k.to_map() if k else None)
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        self.related_resource_filter = []
        if m.get('RelatedResourceFilter') is not None:
            for k in m.get('RelatedResourceFilter'):
                temp_model = ListResourceRelationshipsRequestRelatedResourceFilter()
                self.related_resource_filter.append(temp_model.from_map(k))
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceRelationshipsResponseBodyResourceRelationships(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        related_resource_id: str = None,
        related_resource_region_id: str = None,
        related_resource_type: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The region ID of the resource.
        self.region_id = region_id
        # The ID of the associated resource.
        self.related_resource_id = related_resource_id
        # The region ID of the associated resource.
        self.related_resource_region_id = related_resource_region_id
        # The type of the associated resource.
        self.related_resource_type = related_resource_type
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.related_resource_id is not None:
            result['RelatedResourceId'] = self.related_resource_id
        if self.related_resource_region_id is not None:
            result['RelatedResourceRegionId'] = self.related_resource_region_id
        if self.related_resource_type is not None:
            result['RelatedResourceType'] = self.related_resource_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RelatedResourceId') is not None:
            self.related_resource_id = m.get('RelatedResourceId')
        if m.get('RelatedResourceRegionId') is not None:
            self.related_resource_region_id = m.get('RelatedResourceRegionId')
        if m.get('RelatedResourceType') is not None:
            self.related_resource_type = m.get('RelatedResourceType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceRelationshipsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_relationships: List[ListResourceRelationshipsResponseBodyResourceRelationships] = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The resource relationships.
        self.resource_relationships = resource_relationships

    def validate(self):
        if self.resource_relationships:
            for k in self.resource_relationships:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceRelationships'] = []
        if self.resource_relationships is not None:
            for k in self.resource_relationships:
                result['ResourceRelationships'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_relationships = []
        if m.get('ResourceRelationships') is not None:
            for k in m.get('ResourceRelationships'):
                temp_model = ListResourceRelationshipsResponseBodyResourceRelationships()
                self.resource_relationships.append(temp_model.from_map(k))
        return self


class ListResourceRelationshipsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceRelationshipsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceRelationshipsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        query: List[str] = None,
        resource_type: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language
        # The query conditions.
        self.query = query
        # The resource type.
        # 
        # For more information about the resource types that are supported by Resource Center, see [Services that work with Resource Center](https://help.aliyun.com/document_detail/477798.html).
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.query is not None:
            result['Query'] = self.query
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListResourceTypesResponseBodyResourceTypesCodeMapping(TeaModel):
    def __init__(
        self,
        resource_group: str = None,
        tag: str = None,
    ):
        # The resource group.
        self.resource_group = resource_group
        # The tag.
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group is not None:
            result['ResourceGroup'] = self.resource_group
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroup') is not None:
            self.resource_group = m.get('ResourceGroup')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        code_mapping: ListResourceTypesResponseBodyResourceTypesCodeMapping = None,
        filter_keys: List[str] = None,
        product_name: str = None,
        related_resource_types: List[str] = None,
        resource_type: str = None,
        resource_type_name: str = None,
    ):
        # The code mapping of the resource type.
        self.code_mapping = code_mapping
        # The supported filter conditions.
        self.filter_keys = filter_keys
        # The name of the Alibaba Cloud service.
        self.product_name = product_name
        # The name of supported related resource types.
        self.related_resource_types = related_resource_types
        # The resource type.
        self.resource_type = resource_type
        # The name of the resource type.
        self.resource_type_name = resource_type_name

    def validate(self):
        if self.code_mapping:
            self.code_mapping.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_mapping is not None:
            result['CodeMapping'] = self.code_mapping.to_map()
        if self.filter_keys is not None:
            result['FilterKeys'] = self.filter_keys
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.related_resource_types is not None:
            result['RelatedResourceTypes'] = self.related_resource_types
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.resource_type_name is not None:
            result['ResourceTypeName'] = self.resource_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeMapping') is not None:
            temp_model = ListResourceTypesResponseBodyResourceTypesCodeMapping()
            self.code_mapping = temp_model.from_map(m['CodeMapping'])
        if m.get('FilterKeys') is not None:
            self.filter_keys = m.get('FilterKeys')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('RelatedResourceTypes') is not None:
            self.related_resource_types = m.get('RelatedResourceTypes')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('ResourceTypeName') is not None:
            self.resource_type_name = m.get('ResourceTypeName')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The resource types.
        self.resource_types = resource_types

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['ResourceTypes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_types = []
        if m.get('ResourceTypes') is not None:
            for k in m.get('ResourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSavedQueriesRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
    ):
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 50.
        # 
        # Default value: 50.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListSavedQueriesResponseBodySavedQueries(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        query_id: str = None,
        update_time: str = None,
    ):
        # The time when the template was created. The time is displayed in UTC.
        self.create_time = create_time
        # The description of the template.
        self.description = description
        # The template name.
        self.name = name
        # The template ID.
        self.query_id = query_id
        # The time when the template was updated. The time is displayed in UTC.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.name is not None:
            result['Name'] = self.name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSavedQueriesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        saved_queries: List[ListSavedQueriesResponseBodySavedQueries] = None,
    ):
        # The maximum number of entries per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The information about the custom query templates.
        self.saved_queries = saved_queries

    def validate(self):
        if self.saved_queries:
            for k in self.saved_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SavedQueries'] = []
        if self.saved_queries is not None:
            for k in self.saved_queries:
                result['SavedQueries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.saved_queries = []
        if m.get('SavedQueries') is not None:
            for k in m.get('SavedQueries'):
                temp_model = ListSavedQueriesResponseBodySavedQueries()
                self.saved_queries.append(temp_model.from_map(k))
        return self


class ListSavedQueriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSavedQueriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSavedQueriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        tag_key: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The tag key.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_keys: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag keys.
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_keys is not None:
            result['TagKeys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagKeys') is not None:
            self.tag_keys = m.get('TagKeys')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagValuesRequest(TeaModel):
    def __init__(
        self,
        match_type: str = None,
        max_results: int = None,
        next_token: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The matching mode. Valid values:
        # 
        # *   Equals: equal match
        # *   Prefix: match by prefix
        self.match_type = match_type
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The tag key.
        # 
        # This parameter is required.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagValuesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_values: List[str] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The tag values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_values is not None:
            result['TagValues'] = self.tag_values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')
        return self


class ListTagValuesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagValuesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagValuesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchMultiAccountResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchMultiAccountResourcesRequestSortCriterion(TeaModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
    ):
        # The attribute based on which the entries are sorted.
        # 
        # The value CreateTime indicates the creation time of resources.
        self.key = key
        # The order in which the entries are sorted. Valid values:
        # 
        # *   ASC: The entries are sorted in ascending order. This value is the default value.
        # *   DESC: The entries are sorted in descending order.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SearchMultiAccountResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: List[SearchMultiAccountResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        scope: str = None,
        sort_criterion: SearchMultiAccountResourcesRequestSortCriterion = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries to return on each page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the token to initiate another request and obtain the remaining entries.``
        self.next_token = next_token
        # The search scope. You can set the value to one of the following items:
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched. You can call the [GetResourceDirectory](https://help.aliyun.com/document_detail/159995.html) operation to obtain the ID.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID.
        # *   ID of a folder: Resources within all members in the folder are searched. You can call the [ListFoldersForParent](https://help.aliyun.com/document_detail/159997.html) operation to obtain the ID.
        # *   ID of a member: Resources within the member are searched. You can call the [ListAccounts](https://help.aliyun.com/document_detail/160016.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.scope = scope
        # The method that is used to sort the entries returned.
        self.sort_criterion = sort_criterion

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchMultiAccountResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortCriterion') is not None:
            temp_model = SearchMultiAccountResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m['SortCriterion'])
        return self


class SearchMultiAccountResourcesResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The matching mode.
        self.match_type = match_type
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchMultiAccountResourcesResponseBodyResourcesIpAddressAttributes(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip_address = ip_address
        # The network type. Valid values:
        # 
        # *   **Public**: the Internet
        # *   **Private**: internal network
        self.network_type = network_type
        # The version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class SearchMultiAccountResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchMultiAccountResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[SearchMultiAccountResourcesResponseBodyResourcesIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[SearchMultiAccountResourcesResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        # The ID of the management account or member of the resource directory.
        self.account_id = account_id
        # The time when the resource was created.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The attributes of the IP address.
        self.ip_address_attributes = ip_address_attributes
        # The IP addresses.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The tags.
        self.tags = tags
        # The zone ID.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.ip_address_attributes:
            for k in self.ip_address_attributes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        result['IpAddressAttributes'] = []
        if self.ip_address_attributes is not None:
            for k in self.ip_address_attributes:
                result['IpAddressAttributes'].append(k.to_map() if k else None)
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        self.ip_address_attributes = []
        if m.get('IpAddressAttributes') is not None:
            for k in m.get('IpAddressAttributes'):
                temp_model = SearchMultiAccountResourcesResponseBodyResourcesIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k))
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchMultiAccountResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchMultiAccountResourcesResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[SearchMultiAccountResourcesResponseBodyFilters] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[SearchMultiAccountResourcesResponseBodyResources] = None,
        scope: str = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resources.
        self.resources = resources
        # The search scope.
        # 
        # *   ID of a resource directory: Resources within the management account and all members of the resource directory are searched.
        # *   ID of the Root folder: Resources within all members in the Root folder and the subfolders of the Root folder are searched.
        # *   ID of a folder: Resources within all members in the folder are searched.
        # *   ID of a member: Resources within the member are searched.
        self.scope = scope

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.scope is not None:
            result['Scope'] = self.scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchMultiAccountResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchMultiAccountResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        return self


class SearchMultiAccountResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchMultiAccountResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchMultiAccountResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchResourcesRequestFilter(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        value: List[str] = None,
    ):
        # The key of the filter condition. For more information, see `Supported filter parameters`.
        self.key = key
        # The matching mode.
        # 
        # The value Equals indicates an equal match.
        self.match_type = match_type
        # The values of the filter condition.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesRequestSortCriterion(TeaModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
    ):
        # The attribute based on which the entries are sorted.
        # 
        # The value CreateTime indicates the creation time of resources.
        self.key = key
        # The order in which the entries are sorted. Valid values:
        # 
        # *   ASC: The entries are sorted in ascending order. This value is the default value.
        # *   DESC: The entries are sorted in descending order.
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.order is not None:
            result['Order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Order') is not None:
            self.order = m.get('Order')
        return self


class SearchResourcesRequest(TeaModel):
    def __init__(
        self,
        filter: List[SearchResourcesRequestFilter] = None,
        max_results: int = None,
        next_token: str = None,
        resource_group_id: str = None,
        sort_criterion: SearchResourcesRequestSortCriterion = None,
    ):
        # The filter conditions.
        self.filter = filter
        # The maximum number of entries per page.
        # 
        # Valid values: 1 to 100.
        # 
        # Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        # 
        # If the total number of entries returned for the current request exceeds the value of the `MaxResults` parameter, the entries are truncated. In this case, you can use the `token` to initiate another request and obtain the remaining entries.
        self.next_token = next_token
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The method that is used to sort the entries returned.
        self.sort_criterion = sort_criterion

    def validate(self):
        if self.filter:
            for k in self.filter:
                if k:
                    k.validate()
        if self.sort_criterion:
            self.sort_criterion.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filter'] = []
        if self.filter is not None:
            for k in self.filter:
                result['Filter'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.sort_criterion is not None:
            result['SortCriterion'] = self.sort_criterion.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter = []
        if m.get('Filter') is not None:
            for k in m.get('Filter'):
                temp_model = SearchResourcesRequestFilter()
                self.filter.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SortCriterion') is not None:
            temp_model = SearchResourcesRequestSortCriterion()
            self.sort_criterion = temp_model.from_map(m['SortCriterion'])
        return self


class SearchResourcesResponseBodyFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        match_type: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition.
        self.key = key
        # The matching mode.
        self.match_type = match_type
        # The values of the filter condition.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.match_type is not None:
            result['MatchType'] = self.match_type
        if self.values is not None:
            result['Values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('MatchType') is not None:
            self.match_type = m.get('MatchType')
        if m.get('Values') is not None:
            self.values = m.get('Values')
        return self


class SearchResourcesResponseBodyResourcesIpAddressAttributes(TeaModel):
    def __init__(
        self,
        ip_address: str = None,
        network_type: str = None,
        version: str = None,
    ):
        # The IP address.
        self.ip_address = ip_address
        # The network type. Valid values:
        # 
        # *   **Public**: the Internet
        # *   **Private**: internal network
        self.network_type = network_type
        # The version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address
        if self.network_type is not None:
            result['NetworkType'] = self.network_type
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')
        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class SearchResourcesResponseBodyResourcesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N.
        self.key = key
        # The value of tag N.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SearchResourcesResponseBodyResources(TeaModel):
    def __init__(
        self,
        account_id: str = None,
        create_time: str = None,
        expire_time: str = None,
        ip_address_attributes: List[SearchResourcesResponseBodyResourcesIpAddressAttributes] = None,
        ip_addresses: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        resource_type: str = None,
        tags: List[SearchResourcesResponseBodyResourcesTags] = None,
        zone_id: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.account_id = account_id
        # The time when the resource was created.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.create_time = create_time
        # The time when the resource expires.
        self.expire_time = expire_time
        # The attributes of the IP address.
        self.ip_address_attributes = ip_address_attributes
        # The IP addresses.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.ip_addresses = ip_addresses
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The resource ID.
        self.resource_id = resource_id
        # The resource name.
        self.resource_name = resource_name
        # The resource type.
        self.resource_type = resource_type
        # The tags.
        self.tags = tags
        # The zone ID.
        # 
        # >  Whether this parameter is returned is determined by the Alibaba Cloud service to which the resource belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.ip_address_attributes:
            for k in self.ip_address_attributes:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_id is not None:
            result['AccountId'] = self.account_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        result['IpAddressAttributes'] = []
        if self.ip_address_attributes is not None:
            for k in self.ip_address_attributes:
                result['IpAddressAttributes'].append(k.to_map() if k else None)
        if self.ip_addresses is not None:
            result['IpAddresses'] = self.ip_addresses
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        self.ip_address_attributes = []
        if m.get('IpAddressAttributes') is not None:
            for k in m.get('IpAddressAttributes'):
                temp_model = SearchResourcesResponseBodyResourcesIpAddressAttributes()
                self.ip_address_attributes.append(temp_model.from_map(k))
        if m.get('IpAddresses') is not None:
            self.ip_addresses = m.get('IpAddresses')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = SearchResourcesResponseBodyResourcesTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')
        return self


class SearchResourcesResponseBody(TeaModel):
    def __init__(
        self,
        filters: List[SearchResourcesResponseBodyFilters] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resources: List[SearchResourcesResponseBodyResources] = None,
    ):
        # The filter conditions.
        self.filters = filters
        # The maximum number of entries returned per page.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The ID of the request.
        self.request_id = request_id
        # The information about the resources.
        self.resources = resources

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = SearchResourcesResponseBodyFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = SearchResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k))
        return self


class SearchResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = SearchResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDeliveryChannelRequestDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        resource_types: List[str] = None,
    ):
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class UpdateDeliveryChannelRequestResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class UpdateDeliveryChannelRequestResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        enabled: str = None,
        sls_properties: UpdateDeliveryChannelRequestResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.enabled = enabled
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('SlsProperties') is not None:
            temp_model = UpdateDeliveryChannelRequestResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class UpdateDeliveryChannelRequestResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        enabled: str = None,
        sls_properties: UpdateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.enabled = enabled
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('SlsProperties') is not None:
            temp_model = UpdateDeliveryChannelRequestResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: UpdateDeliveryChannelRequestDeliveryChannelFilter = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        resource_change_delivery: UpdateDeliveryChannelRequestResourceChangeDelivery = None,
        resource_snapshot_delivery: UpdateDeliveryChannelRequestResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_filter = delivery_channel_filter
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = UpdateDeliveryChannelRequestDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = UpdateDeliveryChannelRequestResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = UpdateDeliveryChannelRequestResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class UpdateDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFilterRequest(TeaModel):
    def __init__(
        self,
        filter_configuration: str = None,
        filter_name: str = None,
    ):
        # The configurations of the filter.
        # 
        # This parameter is required.
        self.filter_configuration = filter_configuration
        # The name of the filter.
        # 
        # This parameter is required.
        self.filter_name = filter_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filter_configuration is not None:
            result['FilterConfiguration'] = self.filter_configuration
        if self.filter_name is not None:
            result['FilterName'] = self.filter_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterConfiguration') is not None:
            self.filter_configuration = m.get('FilterConfiguration')
        if m.get('FilterName') is not None:
            self.filter_name = m.get('FilterName')
        return self


class UpdateFilterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateFilterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFilterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateFilterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMultiAccountDeliveryChannelRequestDeliveryChannelFilter(TeaModel):
    def __init__(
        self,
        account_scopes: List[str] = None,
        resource_types: List[str] = None,
    ):
        self.account_scopes = account_scopes
        self.resource_types = resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_scopes is not None:
            result['AccountScopes'] = self.account_scopes
        if self.resource_types is not None:
            result['ResourceTypes'] = self.resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountScopes') is not None:
            self.account_scopes = m.get('AccountScopes')
        if m.get('ResourceTypes') is not None:
            self.resource_types = m.get('ResourceTypes')
        return self


class UpdateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class UpdateMultiAccountDeliveryChannelRequestResourceChangeDelivery(TeaModel):
    def __init__(
        self,
        enabled: str = None,
        sls_properties: UpdateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.enabled = enabled
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('SlsProperties') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelRequestResourceChangeDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties(TeaModel):
    def __init__(
        self,
        oversized_data_oss_target_arn: str = None,
    ):
        self.oversized_data_oss_target_arn = oversized_data_oss_target_arn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oversized_data_oss_target_arn is not None:
            result['OversizedDataOssTargetArn'] = self.oversized_data_oss_target_arn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OversizedDataOssTargetArn') is not None:
            self.oversized_data_oss_target_arn = m.get('OversizedDataOssTargetArn')
        return self


class UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery(TeaModel):
    def __init__(
        self,
        custom_expression: str = None,
        delivery_time: str = None,
        enabled: str = None,
        sls_properties: UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties = None,
        target_arn: str = None,
        target_type: str = None,
    ):
        self.custom_expression = custom_expression
        self.delivery_time = delivery_time
        self.enabled = enabled
        self.sls_properties = sls_properties
        self.target_arn = target_arn
        self.target_type = target_type

    def validate(self):
        if self.sls_properties:
            self.sls_properties.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_expression is not None:
            result['CustomExpression'] = self.custom_expression
        if self.delivery_time is not None:
            result['DeliveryTime'] = self.delivery_time
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.sls_properties is not None:
            result['SlsProperties'] = self.sls_properties.to_map()
        if self.target_arn is not None:
            result['TargetArn'] = self.target_arn
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomExpression') is not None:
            self.custom_expression = m.get('CustomExpression')
        if m.get('DeliveryTime') is not None:
            self.delivery_time = m.get('DeliveryTime')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('SlsProperties') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDeliverySlsProperties()
            self.sls_properties = temp_model.from_map(m['SlsProperties'])
        if m.get('TargetArn') is not None:
            self.target_arn = m.get('TargetArn')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class UpdateMultiAccountDeliveryChannelRequest(TeaModel):
    def __init__(
        self,
        delivery_channel_description: str = None,
        delivery_channel_filter: UpdateMultiAccountDeliveryChannelRequestDeliveryChannelFilter = None,
        delivery_channel_id: str = None,
        delivery_channel_name: str = None,
        resource_change_delivery: UpdateMultiAccountDeliveryChannelRequestResourceChangeDelivery = None,
        resource_snapshot_delivery: UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery = None,
    ):
        self.delivery_channel_description = delivery_channel_description
        self.delivery_channel_filter = delivery_channel_filter
        # This parameter is required.
        self.delivery_channel_id = delivery_channel_id
        self.delivery_channel_name = delivery_channel_name
        self.resource_change_delivery = resource_change_delivery
        self.resource_snapshot_delivery = resource_snapshot_delivery

    def validate(self):
        if self.delivery_channel_filter:
            self.delivery_channel_filter.validate()
        if self.resource_change_delivery:
            self.resource_change_delivery.validate()
        if self.resource_snapshot_delivery:
            self.resource_snapshot_delivery.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.delivery_channel_description is not None:
            result['DeliveryChannelDescription'] = self.delivery_channel_description
        if self.delivery_channel_filter is not None:
            result['DeliveryChannelFilter'] = self.delivery_channel_filter.to_map()
        if self.delivery_channel_id is not None:
            result['DeliveryChannelId'] = self.delivery_channel_id
        if self.delivery_channel_name is not None:
            result['DeliveryChannelName'] = self.delivery_channel_name
        if self.resource_change_delivery is not None:
            result['ResourceChangeDelivery'] = self.resource_change_delivery.to_map()
        if self.resource_snapshot_delivery is not None:
            result['ResourceSnapshotDelivery'] = self.resource_snapshot_delivery.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeliveryChannelDescription') is not None:
            self.delivery_channel_description = m.get('DeliveryChannelDescription')
        if m.get('DeliveryChannelFilter') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelRequestDeliveryChannelFilter()
            self.delivery_channel_filter = temp_model.from_map(m['DeliveryChannelFilter'])
        if m.get('DeliveryChannelId') is not None:
            self.delivery_channel_id = m.get('DeliveryChannelId')
        if m.get('DeliveryChannelName') is not None:
            self.delivery_channel_name = m.get('DeliveryChannelName')
        if m.get('ResourceChangeDelivery') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelRequestResourceChangeDelivery()
            self.resource_change_delivery = temp_model.from_map(m['ResourceChangeDelivery'])
        if m.get('ResourceSnapshotDelivery') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelRequestResourceSnapshotDelivery()
            self.resource_snapshot_delivery = temp_model.from_map(m['ResourceSnapshotDelivery'])
        return self


class UpdateMultiAccountDeliveryChannelResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateMultiAccountDeliveryChannelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMultiAccountDeliveryChannelResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateMultiAccountDeliveryChannelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSavedQueryRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        expression: str = None,
        name: str = None,
        query_id: str = None,
    ):
        # The description of the template.
        # 
        # The description must be 1 to 256 characters in length.
        self.description = description
        # The query statement in the template.
        self.expression = expression
        # The name of the template.
        # 
        # *   The name must be 1 to 64 characters in length.
        # *   The name can contain letters, digits, underscores (_), and hyphens (-).
        # *   The name must be unique.
        self.name = name
        # The template ID.
        # 
        # This parameter is required.
        self.query_id = query_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expression is not None:
            result['Expression'] = self.expression
        if self.name is not None:
            result['Name'] = self.name
        if self.query_id is not None:
            result['QueryId'] = self.query_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Expression') is not None:
            self.expression = m.get('Expression')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('QueryId') is not None:
            self.query_id = m.get('QueryId')
        return self


class UpdateSavedQueryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateSavedQueryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateSavedQueryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateSavedQueryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


