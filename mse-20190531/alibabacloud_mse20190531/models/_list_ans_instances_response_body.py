# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListAnsInstancesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListAnsInstancesResponseBodyData] = None,
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
        # The number of the page to return.
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
                temp_model = main_models.ListAnsInstancesResponseBodyData()
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

class ListAnsInstancesResponseBodyData(DaraModel):
    def __init__(
        self,
        app: str = None,
        cluster_name: str = None,
        datum_key: str = None,
        default_key: str = None,
        enabled: bool = None,
        ephemeral: bool = None,
        fail_count: int = None,
        healthy: bool = None,
        instance_heart_beat_interval: int = None,
        instance_heart_beat_time_out: int = None,
        instance_id: str = None,
        ip: str = None,
        ip_delete_timeout: int = None,
        last_beat: int = None,
        marked: bool = None,
        metadata: Dict[str, Any] = None,
        ok_count: int = None,
        port: int = None,
        service_name: str = None,
        weight: int = None,
    ):
        # The name of the application.
        self.app = app
        # The name of the cluster.
        self.cluster_name = cluster_name
        # The reference key.
        self.datum_key = datum_key
        # The default key.
        self.default_key = default_key
        # The effective status of the instance. Valid values:
        # 
        # *   `true`: The instance takes effect.
        # *   `false`: The instance does not take effect.
        self.enabled = enabled
        # Indicates whether the information about the ephemeral node is obtained. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.ephemeral = ephemeral
        # The number of counted failures.
        self.fail_count = fail_count
        # The health status of the instance. Valid values:
        # 
        # *   `true`: The instance is healthy.
        # *   `false`: The instance is unhealthy.
        self.healthy = healthy
        # The heartbeat interval of the instance. Unit: seconds.
        self.instance_heart_beat_interval = instance_heart_beat_interval
        # The timeout period of the instance heartbeat.
        self.instance_heart_beat_time_out = instance_heart_beat_time_out
        # The ID of the instance.
        self.instance_id = instance_id
        # The public IP address.
        self.ip = ip
        # The timeout period for removing an IP address.
        self.ip_delete_timeout = ip_delete_timeout
        # The last heartbeat time.
        self.last_beat = last_beat
        # Indicates whether the instance was marked. Valid values:
        # 
        # *   `true`: The instance marking was successful.
        # *   `false`: The instance marking failed.
        self.marked = marked
        # The metadata.
        self.metadata = metadata
        # The number of counted successes.
        self.ok_count = ok_count
        # The port number.
        self.port = port
        # The name of the service.
        self.service_name = service_name
        # The weight.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.datum_key is not None:
            result['DatumKey'] = self.datum_key

        if self.default_key is not None:
            result['DefaultKey'] = self.default_key

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.ephemeral is not None:
            result['Ephemeral'] = self.ephemeral

        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.healthy is not None:
            result['Healthy'] = self.healthy

        if self.instance_heart_beat_interval is not None:
            result['InstanceHeartBeatInterval'] = self.instance_heart_beat_interval

        if self.instance_heart_beat_time_out is not None:
            result['InstanceHeartBeatTimeOut'] = self.instance_heart_beat_time_out

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_delete_timeout is not None:
            result['IpDeleteTimeout'] = self.ip_delete_timeout

        if self.last_beat is not None:
            result['LastBeat'] = self.last_beat

        if self.marked is not None:
            result['Marked'] = self.marked

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.ok_count is not None:
            result['OkCount'] = self.ok_count

        if self.port is not None:
            result['Port'] = self.port

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('DatumKey') is not None:
            self.datum_key = m.get('DatumKey')

        if m.get('DefaultKey') is not None:
            self.default_key = m.get('DefaultKey')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('Ephemeral') is not None:
            self.ephemeral = m.get('Ephemeral')

        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('Healthy') is not None:
            self.healthy = m.get('Healthy')

        if m.get('InstanceHeartBeatInterval') is not None:
            self.instance_heart_beat_interval = m.get('InstanceHeartBeatInterval')

        if m.get('InstanceHeartBeatTimeOut') is not None:
            self.instance_heart_beat_time_out = m.get('InstanceHeartBeatTimeOut')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpDeleteTimeout') is not None:
            self.ip_delete_timeout = m.get('IpDeleteTimeout')

        if m.get('LastBeat') is not None:
            self.last_beat = m.get('LastBeat')

        if m.get('Marked') is not None:
            self.marked = m.get('Marked')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('OkCount') is not None:
            self.ok_count = m.get('OkCount')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

