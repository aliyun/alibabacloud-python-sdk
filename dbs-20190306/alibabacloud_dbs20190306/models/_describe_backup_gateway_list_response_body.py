# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dbs20190306 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupGatewayListResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        items: main_models.DescribeBackupGatewayListResponseBodyItems = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_elements: int = None,
        total_pages: int = None,
    ):
        # The error code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        self.items = items
        # The page number.
        self.page_num = page_num
        # The number of records on each page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The total number of backup gateways.
        self.total_elements = total_elements
        # The total number of pages.
        self.total_pages = total_pages

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_num is not None:
            result['PageNum'] = self.page_num

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_elements is not None:
            result['TotalElements'] = self.total_elements

        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Items') is not None:
            temp_model = main_models.DescribeBackupGatewayListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalElements') is not None:
            self.total_elements = m.get('TotalElements')

        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')

        return self

class DescribeBackupGatewayListResponseBodyItems(DaraModel):
    def __init__(
        self,
        backup_gateway: List[main_models.DescribeBackupGatewayListResponseBodyItemsBackupGateway] = None,
    ):
        self.backup_gateway = backup_gateway

    def validate(self):
        if self.backup_gateway:
            for v1 in self.backup_gateway:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupGateway'] = []
        if self.backup_gateway is not None:
            for k1 in self.backup_gateway:
                result['BackupGateway'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_gateway = []
        if m.get('BackupGateway') is not None:
            for k1 in m.get('BackupGateway'):
                temp_model = main_models.DescribeBackupGatewayListResponseBodyItemsBackupGateway()
                self.backup_gateway.append(temp_model.from_map(k1))

        return self



class DescribeBackupGatewayListResponseBodyItemsBackupGateway(DaraModel):
    def __init__(
        self,
        backup_gateway_create_time: int = None,
        backup_gateway_id: str = None,
        backup_gateway_status: str = None,
        display_name: str = None,
        identifier: str = None,
        last_heartbeat_time: int = None,
        region: str = None,
        source_endpoint_hostname: str = None,
        source_endpoint_internet_ip: str = None,
        source_endpoint_intranet_ip: str = None,
    ):
        self.backup_gateway_create_time = backup_gateway_create_time
        self.backup_gateway_id = backup_gateway_id
        self.backup_gateway_status = backup_gateway_status
        self.display_name = display_name
        self.identifier = identifier
        self.last_heartbeat_time = last_heartbeat_time
        self.region = region
        self.source_endpoint_hostname = source_endpoint_hostname
        self.source_endpoint_internet_ip = source_endpoint_internet_ip
        self.source_endpoint_intranet_ip = source_endpoint_intranet_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_gateway_create_time is not None:
            result['BackupGatewayCreateTime'] = self.backup_gateway_create_time

        if self.backup_gateway_id is not None:
            result['BackupGatewayId'] = self.backup_gateway_id

        if self.backup_gateway_status is not None:
            result['BackupGatewayStatus'] = self.backup_gateway_status

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.last_heartbeat_time is not None:
            result['LastHeartbeatTime'] = self.last_heartbeat_time

        if self.region is not None:
            result['Region'] = self.region

        if self.source_endpoint_hostname is not None:
            result['SourceEndpointHostname'] = self.source_endpoint_hostname

        if self.source_endpoint_internet_ip is not None:
            result['SourceEndpointInternetIP'] = self.source_endpoint_internet_ip

        if self.source_endpoint_intranet_ip is not None:
            result['SourceEndpointIntranetIP'] = self.source_endpoint_intranet_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupGatewayCreateTime') is not None:
            self.backup_gateway_create_time = m.get('BackupGatewayCreateTime')

        if m.get('BackupGatewayId') is not None:
            self.backup_gateway_id = m.get('BackupGatewayId')

        if m.get('BackupGatewayStatus') is not None:
            self.backup_gateway_status = m.get('BackupGatewayStatus')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('LastHeartbeatTime') is not None:
            self.last_heartbeat_time = m.get('LastHeartbeatTime')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('SourceEndpointHostname') is not None:
            self.source_endpoint_hostname = m.get('SourceEndpointHostname')

        if m.get('SourceEndpointInternetIP') is not None:
            self.source_endpoint_internet_ip = m.get('SourceEndpointInternetIP')

        if m.get('SourceEndpointIntranetIP') is not None:
            self.source_endpoint_intranet_ip = m.get('SourceEndpointIntranetIP')

        return self

