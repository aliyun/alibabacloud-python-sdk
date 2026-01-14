# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListEurekaInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListEurekaInstancesResponseBodyData] = None,
        error_code: str = None,
        http_code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The details of the data.
        self.data = data
        # The error code returned if the request failed.
        self.error_code = error_code
        # The HTTP status code returned.
        self.http_code = http_code
        # The message returned.
        self.message = message
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   `true`: The request was successful.
        # *   `false`: The request failed.
        self.success = success
        # The total number of returned instances.
        self.total_count = total_count

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

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListEurekaInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListEurekaInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        app: str = None,
        duration_in_secs: int = None,
        home_page_url: str = None,
        host_name: str = None,
        instance_id: str = None,
        ip_addr: str = None,
        last_dirty_timestamp: int = None,
        last_updated_timestamp: int = None,
        metadata: Dict[str, Any] = None,
        port: int = None,
        renewal_interval_in_secs: int = None,
        secure_port: int = None,
        status: str = None,
        vip_address: str = None,
    ):
        # The name of the application.
        self.app = app
        # The timeout period of the instance.\\
        # After the specified timeout period expires, the service is unavailable by default and is deleted.
        self.duration_in_secs = duration_in_secs
        # The URL of the homepage.
        self.home_page_url = home_page_url
        # The hostname.
        self.host_name = host_name
        # The ID of the instance.
        self.instance_id = instance_id
        # The IP address.
        self.ip_addr = ip_addr
        # The time when the instance was last modified.
        self.last_dirty_timestamp = last_dirty_timestamp
        # The time when the instance heartbeat was last checked.
        self.last_updated_timestamp = last_updated_timestamp
        # The metadata.
        self.metadata = metadata
        # The service port number.
        self.port = port
        # The maximum interval between two heartbeat checks after a heartbeat check times out.\\
        # Default value: 10.
        self.renewal_interval_in_secs = renewal_interval_in_secs
        # The security port.
        self.secure_port = secure_port
        # The number of service providers. The value is in the following format: Number of healthy instances/Total number of instances.
        self.status = status
        # The virtual IP address (VIP).
        self.vip_address = vip_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.duration_in_secs is not None:
            result['DurationInSecs'] = self.duration_in_secs

        if self.home_page_url is not None:
            result['HomePageUrl'] = self.home_page_url

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip_addr is not None:
            result['IpAddr'] = self.ip_addr

        if self.last_dirty_timestamp is not None:
            result['LastDirtyTimestamp'] = self.last_dirty_timestamp

        if self.last_updated_timestamp is not None:
            result['LastUpdatedTimestamp'] = self.last_updated_timestamp

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.port is not None:
            result['Port'] = self.port

        if self.renewal_interval_in_secs is not None:
            result['RenewalIntervalInSecs'] = self.renewal_interval_in_secs

        if self.secure_port is not None:
            result['SecurePort'] = self.secure_port

        if self.status is not None:
            result['Status'] = self.status

        if self.vip_address is not None:
            result['VipAddress'] = self.vip_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('DurationInSecs') is not None:
            self.duration_in_secs = m.get('DurationInSecs')

        if m.get('HomePageUrl') is not None:
            self.home_page_url = m.get('HomePageUrl')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IpAddr') is not None:
            self.ip_addr = m.get('IpAddr')

        if m.get('LastDirtyTimestamp') is not None:
            self.last_dirty_timestamp = m.get('LastDirtyTimestamp')

        if m.get('LastUpdatedTimestamp') is not None:
            self.last_updated_timestamp = m.get('LastUpdatedTimestamp')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RenewalIntervalInSecs') is not None:
            self.renewal_interval_in_secs = m.get('RenewalIntervalInSecs')

        if m.get('SecurePort') is not None:
            self.secure_port = m.get('SecurePort')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('VipAddress') is not None:
            self.vip_address = m.get('VipAddress')

        return self

