# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ons20190214 import models as main_models
from darabonba.model import DaraModel

class OnsInstanceBaseInfoResponseBody(DaraModel):
    def __init__(
        self,
        instance_base_info: main_models.OnsInstanceBaseInfoResponseBodyInstanceBaseInfo = None,
        request_id: str = None,
    ):
        # The information about the instance.
        self.instance_base_info = instance_base_info
        # The ID of the request. This parameter is a common parameter. Each request has a unique ID. You can use this ID to troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.instance_base_info:
            self.instance_base_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_base_info is not None:
            result['InstanceBaseInfo'] = self.instance_base_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceBaseInfo') is not None:
            temp_model = main_models.OnsInstanceBaseInfoResponseBodyInstanceBaseInfo()
            self.instance_base_info = temp_model.from_map(m.get('InstanceBaseInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class OnsInstanceBaseInfoResponseBodyInstanceBaseInfo(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        endpoints: main_models.OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints = None,
        independent_naming: bool = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_status: int = None,
        instance_type: int = None,
        max_tps: int = None,
        release_time: int = None,
        remark: str = None,
        support_classic: int = None,
        topic_capacity: int = None,
        sp_instance_id: str = None,
        sp_instance_type: int = None,
    ):
        # The time when the instance was created. The value of this parameter is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The endpoints used to access ApsaraMQ for RocketMQ over different protocols.
        self.endpoints = endpoints
        # Indicates whether the instance uses a namespace. Valid values:
        # 
        # *   **true**: The instance uses a separate namespace. The name of each resource must be unique in the instance. The names of resources in different instances can be the same.
        # *   **false**: The instance does not use a separate namespace. The name of each resource must be globally unique within the instance and across all instances.
        self.independent_naming = independent_naming
        # The ID of the instance
        self.instance_id = instance_id
        # The name of the instance.
        # 
        # The name must be 3 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.instance_name = instance_name
        # The status of the instance. Valid values:
        # 
        # *   **0**: The instance is being deployed. This value is valid only for Enterprise Platinum Edition instances.
        # *   **2**: The instance has overdue payments. This value is valid only for Standard Edition instances.
        # *   **5**: The instance is running. This value is valid for Standard Edition instances and Enterprise Platinum Edition instances.
        # *   **7**: The instance is being upgraded and is running. This value is valid only for Enterprise Platinum Edition instances.
        self.instance_status = instance_status
        # The instance type. Valid values:
        # 
        # *   **1**: Standard Edition instances that use the pay-as-you-go billing method.
        # *   **2**: Enterprise Platinum Edition instances that use the subscription billing method.
        # 
        # For information about the editions and specifications of ApsaraMQ for RocketMQ instances, see [Instance editions](https://help.aliyun.com/document_detail/185261.html).
        self.instance_type = instance_type
        # The maximum messaging transactions per second (TPS). Valid values: 5000, 10000, 20000, 50000, 100000, 200000, 300000, 500000, 800000, and 1000000.
        # 
        # You can view the details about messaging TPS on the buy page of ApsaraMQ for RocketMQ.
        # 
        # > This parameter is available only to the ApsaraMQ for RocketMQ Enterprise Platinum Edition instances.
        self.max_tps = max_tps
        # The time when the Enterprise Platinum Edition instance expires.
        self.release_time = release_time
        # The description of the instance.
        self.remark = remark
        self.support_classic = support_classic
        # The maximum number of topics that can be created on the instance. Valid values: 25, 50, 100, 300, and 500.
        # 
        # > This parameter is available only to the ApsaraMQ for RocketMQ Enterprise Platinum Edition instances.
        self.topic_capacity = topic_capacity
        # The commodity ID of the instance.
        self.sp_instance_id = sp_instance_id
        # The commodity type of the instance.
        self.sp_instance_type = sp_instance_type

    def validate(self):
        if self.endpoints:
            self.endpoints.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.endpoints is not None:
            result['Endpoints'] = self.endpoints.to_map()

        if self.independent_naming is not None:
            result['IndependentNaming'] = self.independent_naming

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_tps is not None:
            result['MaxTps'] = self.max_tps

        if self.release_time is not None:
            result['ReleaseTime'] = self.release_time

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.support_classic is not None:
            result['SupportClassic'] = self.support_classic

        if self.topic_capacity is not None:
            result['TopicCapacity'] = self.topic_capacity

        if self.sp_instance_id is not None:
            result['spInstanceId'] = self.sp_instance_id

        if self.sp_instance_type is not None:
            result['spInstanceType'] = self.sp_instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Endpoints') is not None:
            temp_model = main_models.OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints()
            self.endpoints = temp_model.from_map(m.get('Endpoints'))

        if m.get('IndependentNaming') is not None:
            self.independent_naming = m.get('IndependentNaming')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxTps') is not None:
            self.max_tps = m.get('MaxTps')

        if m.get('ReleaseTime') is not None:
            self.release_time = m.get('ReleaseTime')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('SupportClassic') is not None:
            self.support_classic = m.get('SupportClassic')

        if m.get('TopicCapacity') is not None:
            self.topic_capacity = m.get('TopicCapacity')

        if m.get('spInstanceId') is not None:
            self.sp_instance_id = m.get('spInstanceId')

        if m.get('spInstanceType') is not None:
            self.sp_instance_type = m.get('spInstanceType')

        return self

class OnsInstanceBaseInfoResponseBodyInstanceBaseInfoEndpoints(DaraModel):
    def __init__(
        self,
        http_internal_endpoint: str = None,
        http_internet_endpoint: str = None,
        http_internet_secure_endpoint: str = None,
        tcp_endpoint: str = None,
        tcp_internet_endpoint: str = None,
    ):
        # The private HTTP endpoint of the instance.
        self.http_internal_endpoint = http_internal_endpoint
        # The public HTTP endpoint of the instance.
        self.http_internet_endpoint = http_internet_endpoint
        # The public HTTPS endpoint of the instance.
        self.http_internet_secure_endpoint = http_internet_secure_endpoint
        # The private TCP endpoint of the instance.
        self.tcp_endpoint = tcp_endpoint
        # The public TCP endpoint of the instance.
        # 
        # *   Only instances that are deployed in the China (Chengdu), China (Qingdao), or China (Shenzhen) region can be accessed by using public TCP endpoints.
        # 
        # *   Before you use a public TCP endpoint, make sure that your client SDK meets the following requirements:
        # 
        #     *   TCP client SDK for Java: V2.0.0.Final or later For more information, see [Release notes for the SDK for Java](https://help.aliyun.com/document_detail/325569.html).
        #     *   TCP client SDK for C++: V3.0.0 or later For more information, see [Release notes for the SDK for C++](https://help.aliyun.com/document_detail/325570.html).
        # 
        # *   You are charged for Internet traffic when you use a public TCP endpoint. For more information, see [Internet traffic fee](https://help.aliyun.com/document_detail/325571.html).
        self.tcp_internet_endpoint = tcp_internet_endpoint

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.http_internal_endpoint is not None:
            result['HttpInternalEndpoint'] = self.http_internal_endpoint

        if self.http_internet_endpoint is not None:
            result['HttpInternetEndpoint'] = self.http_internet_endpoint

        if self.http_internet_secure_endpoint is not None:
            result['HttpInternetSecureEndpoint'] = self.http_internet_secure_endpoint

        if self.tcp_endpoint is not None:
            result['TcpEndpoint'] = self.tcp_endpoint

        if self.tcp_internet_endpoint is not None:
            result['TcpInternetEndpoint'] = self.tcp_internet_endpoint

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HttpInternalEndpoint') is not None:
            self.http_internal_endpoint = m.get('HttpInternalEndpoint')

        if m.get('HttpInternetEndpoint') is not None:
            self.http_internet_endpoint = m.get('HttpInternetEndpoint')

        if m.get('HttpInternetSecureEndpoint') is not None:
            self.http_internet_secure_endpoint = m.get('HttpInternetSecureEndpoint')

        if m.get('TcpEndpoint') is not None:
            self.tcp_endpoint = m.get('TcpEndpoint')

        if m.get('TcpInternetEndpoint') is not None:
            self.tcp_internet_endpoint = m.get('TcpInternetEndpoint')

        return self

