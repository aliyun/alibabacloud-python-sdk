# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDtsJobsRequest(DaraModel):
    def __init__(
        self,
        dedicated_cluster_id: str = None,
        dest_product_type: str = None,
        dts_bis_label: str = None,
        dts_instance_id: str = None,
        dts_job_id: str = None,
        group_id: str = None,
        instance_id: str = None,
        instance_type: str = None,
        job_type: str = None,
        order_column: str = None,
        order_direction: str = None,
        owner_id: str = None,
        page_number: int = None,
        page_size: int = None,
        params: str = None,
        region: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        src_product_type: str = None,
        status: str = None,
        tags: str = None,
        type: str = None,
        without_db_list: bool = None,
        zero_etl_job: bool = None,
    ):
        # The ID of the DTS dedicated cluster on which the task runs.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The type of the source database instance.
        self.dest_product_type = dest_product_type
        # The environment tag of the DTS instance. Valid values:
        # 
        # - **normal**
        # - **online**
        self.dts_bis_label = dts_bis_label
        # The ID of the data migration, data synchronization, or change tracking instance.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        self.dts_job_id = dts_job_id
        # The ID of the parent task.
        # 
        # >  In most cases, you do not need to specify this parameter.
        self.group_id = group_id
        # The ID of the source or target database instance corresponding to the request parameter **InstanceType**.
        self.instance_id = instance_id
        # The type of the source or target database instance.
        self.instance_type = instance_type
        # The type of the DTS task. Valid values:
        # 
        # *   **MIGRATION**: data migration. This is the default value.
        # *   **SYNC**: data synchronization.
        # *   **SUBSCRIBE**: change tracking.
        self.job_type = job_type
        # The basis on which the returned DTS tasks are sorted. Valid values:
        # 
        # *   **CreateTime**: sorts the DTS tasks based on the points in time when the DTS tasks are created.
        # *   **FinishTime**: sorts the DTS tasks based on the points in time when the DTS tasks are complete.
        # *   **duLimit** sorts the DTS tasks based on the upper limits on DTS Units (DUs) that the DTS tasks can use. This option applies only to the DTS tasks that are run on a DTS dedicated cluster.
        # 
        # >  You can also set the **OrderDirection** parameter to specify whether to sort the DTS tasks in ascending or descending order.
        self.order_column = order_column
        # The order in which the returned DTS tasks are sorted. Valid values:
        # 
        # *   **ASC**: sorts the DTS tasks in ascending order. This is the default value.
        # *   **DESC**: sorts the DTS tasks in descending order.
        self.order_direction = order_direction
        self.owner_id = owner_id
        # The page number. Pages start from page **1**. Default value: **1**.
        self.page_number = page_number
        # The number of entries per page. Valid values: **20**, **30**, **50**, and **100**. Default value: **20**.
        self.page_size = page_size
        # The content of the query condition.
        # 
        # >  You must set the **Type** parameter to specify the type of the query condition.
        self.params = params
        # The ID of the region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # This parameter is deprecated.
        # 
        # Valid values:
        # 
        # *   cn-hangzhou
        # *   cn-shanghai
        # *   cn-beijing
        # *   cn-guangzhou
        # *   cn-shenzhen
        # *   cn-chengdu
        # *   cn-heyuan
        # *   cn-hongkong
        # *   cn-qingdao
        # *   cn-zhangbei
        # *   cn-zhangjiakou
        # *   us-east-1
        # *   us-west-1
        # *   cn-hangzhou-finance
        # *   cn-shanghai-finance
        # *   cn-shanghai-finance-1
        # *   cn-shenzhen-finance
        # *   cn-shenzhen-finance-1
        # *   cn-beijing-finance-1
        # *   cn-huhehaote
        # *   cn-north-2-gov-1
        # *   eu-central-1
        # *   eu-west-1
        # *   me-central-1
        # *   me-east-1
        # *   ap-northeast-1
        # *   ap-northeast-2
        # *   ap-southeast-1
        # *   ap-southeast-2
        # *   ap-southeast-3
        # *   ap-southeast-5
        # *   ap-southeast-6
        # *   ap-southeast-7
        # *   cn-wulanchabu
        # *   cn-zhengzhou-jva
        # *   cn-wuhan-lr
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of the destination database instance.
        self.src_product_type = src_product_type
        # The state of the DTS task.
        # 
        # Valid values for a data migration task:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **NotConfigured**: The task is not configured.
        # *   **Migrating**: The task is in progress.
        # *   **Suspending**: The task is paused.
        # *   **MigrationFailed**: The task failed.
        # *   **Finished**: The task is complete.
        # *   **Retrying**: The task is being retried.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        # 
        # Valid values for a data synchronization task:
        # 
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **NotConfigured**: The task is not configured.
        # *   **Initializing**: The task is being initialized.
        # *   **InitializeFailed**: Initialization failed.
        # *   **Synchronizing**: The task is in progress.
        # *   **Failed**: The task failed.
        # *   **Suspending**: The task is paused.
        # *   **Modifying**: The objects in the task are being modified.
        # *   **Finished**: The task is complete.
        # *   **Retrying**: The task is being retried.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        # 
        # Valid values for a change tracking task:
        # 
        # *   **NotConfigured**: The task is not configured.
        # *   **NotStarted**: The task is not started.
        # *   **Prechecking**: The task is being prechecked.
        # *   **PrecheckFailed**: The task failed to pass the precheck.
        # *   **PreCheckPass**: The task passed the precheck.
        # *   **Starting**: The task is being started.
        # *   **Normal**: The task is running as expected.
        # *   **Retrying**: The task is being retried.
        # *   **Abnormal**: The task is not running as expected.
        # *   **Upgrade**: The task is being upgraded.
        # *   **Locked**: The task is locked.
        # *   **Downgrade**: The task is being downgraded.
        self.status = status
        # The tags of the DTS task to be queried. Specify tags in the JSON format.
        # 
        # >  You can call the **ListTagResources** operation to query the tag key and tag value.
        self.tags = tags
        # The type of the query condition. Valid values:
        # 
        # *   **instance**: queries DTS tasks based on the ID of a DTS instance.
        # *   **name**: queries DTS tasks based on the name of a DTS instance. Fuzzy match is supported.
        # *   **srcRds**: queries DTS tasks based on the ID of an ApsaraDB RDS instance. The ApsaraDB RDS instance is the source instance of a DTS task.
        # *   **rds**: queries DTS tasks based on the ID of an ApsaraDB RDS instance. The ApsaraDB RDS instance is the destination instance of a DTS task.
        # 
        # >  You must set the **Params** parameter to specify the content of the query condition.
        self.type = type
        # Specifies whether to skip the **DbObject** parameter in the response. The DbObject parameter specifies the objects of the data migration, data synchronization, or change tracking task. Valid values:
        # 
        # - **true**: does not return **DbObject**.
        # - **false**: returns **DbObject**. If you set this parameter to false, the response time is shortened.
        self.without_db_list = without_db_list
        # Whether it is a seamless integration (Zero-ETL) task, the value can be:
        # - **false**: No. - **true**: Yes.
        self.zero_etl_job = zero_etl_job

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_cluster_id is not None:
            result['DedicatedClusterId'] = self.dedicated_cluster_id

        if self.dest_product_type is not None:
            result['DestProductType'] = self.dest_product_type

        if self.dts_bis_label is not None:
            result['DtsBisLabel'] = self.dts_bis_label

        if self.dts_instance_id is not None:
            result['DtsInstanceId'] = self.dts_instance_id

        if self.dts_job_id is not None:
            result['DtsJobId'] = self.dts_job_id

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.order_column is not None:
            result['OrderColumn'] = self.order_column

        if self.order_direction is not None:
            result['OrderDirection'] = self.order_direction

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.params is not None:
            result['Params'] = self.params

        if self.region is not None:
            result['Region'] = self.region

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.src_product_type is not None:
            result['SrcProductType'] = self.src_product_type

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.type is not None:
            result['Type'] = self.type

        if self.without_db_list is not None:
            result['WithoutDbList'] = self.without_db_list

        if self.zero_etl_job is not None:
            result['ZeroEtlJob'] = self.zero_etl_job

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedClusterId') is not None:
            self.dedicated_cluster_id = m.get('DedicatedClusterId')

        if m.get('DestProductType') is not None:
            self.dest_product_type = m.get('DestProductType')

        if m.get('DtsBisLabel') is not None:
            self.dts_bis_label = m.get('DtsBisLabel')

        if m.get('DtsInstanceId') is not None:
            self.dts_instance_id = m.get('DtsInstanceId')

        if m.get('DtsJobId') is not None:
            self.dts_job_id = m.get('DtsJobId')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('OrderColumn') is not None:
            self.order_column = m.get('OrderColumn')

        if m.get('OrderDirection') is not None:
            self.order_direction = m.get('OrderDirection')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SrcProductType') is not None:
            self.src_product_type = m.get('SrcProductType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('WithoutDbList') is not None:
            self.without_db_list = m.get('WithoutDbList')

        if m.get('ZeroEtlJob') is not None:
            self.zero_etl_job = m.get('ZeroEtlJob')

        return self

