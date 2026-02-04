# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeSubscriptionInstancesResponseBody(DaraModel):
    def __init__(
        self,
        err_code: str = None,
        err_message: str = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        subscription_instances: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstances = None,
        success: str = None,
        total_record_count: int = None,
    ):
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The page number of the returned page.
        self.page_number = page_number
        # The maximum number of entries that can be displayed on the current page.
        self.page_record_count = page_record_count
        # The ID of the request.
        self.request_id = request_id
        # The list of change tracking instances and the details of each instance.
        self.subscription_instances = subscription_instances
        # Indicates whether the call was successful.
        self.success = success
        # The total number of change tracking instances that belong to your Alibaba Cloud account.
        self.total_record_count = total_record_count

    def validate(self):
        if self.subscription_instances:
            self.subscription_instances.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subscription_instances is not None:
            result['SubscriptionInstances'] = self.subscription_instances.to_map()

        if self.success is not None:
            result['Success'] = self.success

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubscriptionInstances') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstances()
            self.subscription_instances = temp_model.from_map(m.get('SubscriptionInstances'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstances(DaraModel):
    def __init__(
        self,
        subscription_instance: List[main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance] = None,
    ):
        self.subscription_instance = subscription_instance

    def validate(self):
        if self.subscription_instance:
            for v1 in self.subscription_instance:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SubscriptionInstance'] = []
        if self.subscription_instance is not None:
            for k1 in self.subscription_instance:
                result['SubscriptionInstance'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.subscription_instance = []
        if m.get('SubscriptionInstance') is not None:
            for k1 in m.get('SubscriptionInstance'):
                temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance()
                self.subscription_instance.append(temp_model.from_map(k1))

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstance(DaraModel):
    def __init__(
        self,
        begin_timestamp: str = None,
        consumption_checkpoint: str = None,
        consumption_client: str = None,
        end_timestamp: str = None,
        error_message: str = None,
        instance_create_time: str = None,
        job_create_time: str = None,
        pay_type: str = None,
        source_endpoint: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint = None,
        status: str = None,
        subscribe_topic: str = None,
        subscription_data_type: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType = None,
        subscription_host: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        subscription_object: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject = None,
        tags: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags = None,
    ):
        # The start of the time range for change tracking. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.begin_timestamp = begin_timestamp
        # The consumption checkpoint of the change tracking instance. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.consumption_checkpoint = consumption_checkpoint
        # The downstream client information, in the following format: \\<IP address of the downstream client>:\\<Random ID generated by DTS>.
        self.consumption_client = consumption_client
        # The end of the time range for change tracking. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.end_timestamp = end_timestamp
        # The error message returned if change tracking failed.
        self.error_message = error_message
        # The time when the change tracking instance was created. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC.
        self.instance_create_time = instance_create_time
        # The time when the change tracking task was created. The time is displayed in the *yyyy-MM-dd*T*HH:mm:ss*Z format in UTC.
        self.job_create_time = job_create_time
        # The billing method of the change tracking instance. Valid values:
        # 
        # *   **PrePaid**: subscription
        # *   **PostPaid**: pay-as-you-go
        self.pay_type = pay_type
        # The connection settings of the source instance.
        self.source_endpoint = source_endpoint
        # The status of the change tracking task. Valid values:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **Starting**: The task is being started.
        # *   **Normal**: The task is running as expected.
        # *   **Abnormal**: The task is not running as expected.
        self.status = status
        # The topic of the change tracking instance.
        # 
        # >  This parameter is returned only if your change tracking instances are of the new version and you have called the [CreateConsumerGroup](https://help.aliyun.com/document_detail/122863.html) operation to create a consumer group.
        self.subscribe_topic = subscribe_topic
        # The types of operations that are tracked by the task.
        self.subscription_data_type = subscription_data_type
        # The endpoint of the change tracking instance.
        self.subscription_host = subscription_host
        # The ID of the change tracking instance.
        self.subscription_instance_id = subscription_instance_id
        # The name of the change tracking instance.
        self.subscription_instance_name = subscription_instance_name
        # The objects for change tracking.
        self.subscription_object = subscription_object
        # The collection of tags.
        self.tags = tags

    def validate(self):
        if self.source_endpoint:
            self.source_endpoint.validate()
        if self.subscription_data_type:
            self.subscription_data_type.validate()
        if self.subscription_host:
            self.subscription_host.validate()
        if self.subscription_object:
            self.subscription_object.validate()
        if self.tags:
            self.tags.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_timestamp is not None:
            result['BeginTimestamp'] = self.begin_timestamp

        if self.consumption_checkpoint is not None:
            result['ConsumptionCheckpoint'] = self.consumption_checkpoint

        if self.consumption_client is not None:
            result['ConsumptionClient'] = self.consumption_client

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.instance_create_time is not None:
            result['InstanceCreateTime'] = self.instance_create_time

        if self.job_create_time is not None:
            result['JobCreateTime'] = self.job_create_time

        if self.pay_type is not None:
            result['PayType'] = self.pay_type

        if self.source_endpoint is not None:
            result['SourceEndpoint'] = self.source_endpoint.to_map()

        if self.status is not None:
            result['Status'] = self.status

        if self.subscribe_topic is not None:
            result['SubscribeTopic'] = self.subscribe_topic

        if self.subscription_data_type is not None:
            result['SubscriptionDataType'] = self.subscription_data_type.to_map()

        if self.subscription_host is not None:
            result['SubscriptionHost'] = self.subscription_host.to_map()

        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id

        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name

        if self.subscription_object is not None:
            result['SubscriptionObject'] = self.subscription_object.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginTimestamp') is not None:
            self.begin_timestamp = m.get('BeginTimestamp')

        if m.get('ConsumptionCheckpoint') is not None:
            self.consumption_checkpoint = m.get('ConsumptionCheckpoint')

        if m.get('ConsumptionClient') is not None:
            self.consumption_client = m.get('ConsumptionClient')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('InstanceCreateTime') is not None:
            self.instance_create_time = m.get('InstanceCreateTime')

        if m.get('JobCreateTime') is not None:
            self.job_create_time = m.get('JobCreateTime')

        if m.get('PayType') is not None:
            self.pay_type = m.get('PayType')

        if m.get('SourceEndpoint') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint()
            self.source_endpoint = temp_model.from_map(m.get('SourceEndpoint'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubscribeTopic') is not None:
            self.subscribe_topic = m.get('SubscribeTopic')

        if m.get('SubscriptionDataType') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType()
            self.subscription_data_type = temp_model.from_map(m.get('SubscriptionDataType'))

        if m.get('SubscriptionHost') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost()
            self.subscription_host = temp_model.from_map(m.get('SubscriptionHost'))

        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')

        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')

        if m.get('SubscriptionObject') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject()
            self.subscription_object = temp_model.from_map(m.get('SubscriptionObject'))

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceTagsTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value that corresponds to the tag key.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObject(DaraModel):
    def __init__(
        self,
        synchronous_object: List[main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject] = None,
    ):
        self.synchronous_object = synchronous_object

    def validate(self):
        if self.synchronous_object:
            for v1 in self.synchronous_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SynchronousObject'] = []
        if self.synchronous_object is not None:
            for k1 in self.synchronous_object:
                result['SynchronousObject'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.synchronous_object = []
        if m.get('SynchronousObject') is not None:
            for k1 in m.get('SynchronousObject'):
                temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject()
                self.synchronous_object.append(temp_model.from_map(k1))

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObject(DaraModel):
    def __init__(
        self,
        database_name: str = None,
        table_list: main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList = None,
        whole_database: str = None,
    ):
        # The name of the database to which the object belongs.
        self.database_name = database_name
        # The table name.
        self.table_list = table_list
        # Indicates whether the data of an entire database is tracked. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.whole_database = whole_database

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()

        if self.whole_database is not None:
            result['WholeDatabase'] = self.whole_database

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('TableList') is not None:
            temp_model = main_models.DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList()
            self.table_list = temp_model.from_map(m.get('TableList'))

        if m.get('WholeDatabase') is not None:
            self.whole_database = m.get('WholeDatabase')

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionObjectSynchronousObjectTableList(DaraModel):
    def __init__(
        self,
        table: List[str] = None,
    ):
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionHost(DaraModel):
    def __init__(
        self,
        private_host: str = None,
        public_host: str = None,
        vpchost: str = None,
    ):
        # The private endpoint of the change tracking instance. The format is `<Address>:<Port number>`.
        self.private_host = private_host
        # The public endpoint of the change tracking instance. The format is `<Address>:<Port number>`.
        self.public_host = public_host
        # The virtual private cloud (VPC) endpoint of the change tracking instance. The format is `<Address>:<Port number>`.
        self.vpchost = vpchost

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_host is not None:
            result['PrivateHost'] = self.private_host

        if self.public_host is not None:
            result['PublicHost'] = self.public_host

        if self.vpchost is not None:
            result['VPCHost'] = self.vpchost

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateHost') is not None:
            self.private_host = m.get('PrivateHost')

        if m.get('PublicHost') is not None:
            self.public_host = m.get('PublicHost')

        if m.get('VPCHost') is not None:
            self.vpchost = m.get('VPCHost')

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSubscriptionDataType(DaraModel):
    def __init__(
        self,
        ddl: bool = None,
        dml: bool = None,
    ):
        # Indicates whether data definition language (DDL) operations are tracked. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.ddl = ddl
        # Indicates whether data manipulation language (DML) operations are tracked. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.dml = dml

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl is not None:
            result['DDL'] = self.ddl

        if self.dml is not None:
            result['DML'] = self.dml

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')

        if m.get('DML') is not None:
            self.dml = m.get('DML')

        return self

class DescribeSubscriptionInstancesResponseBodySubscriptionInstancesSubscriptionInstanceSourceEndpoint(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_type: str = None,
    ):
        # The ID of the source instance.
        self.instance_id = instance_id
        # The type of the source instance.
        # 
        # >  This parameter is returned only for change tracking instances of the new version.
        self.instance_type = instance_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceID'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceID') is not None:
            self.instance_id = m.get('InstanceID')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        return self

