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
        # The ID of the DTS dedicated cluster.
        self.dedicated_cluster_id = dedicated_cluster_id
        # The type of the source database instance.
        self.dest_product_type = dest_product_type
        # The environment label of the DTS instance. Valid values:
        # - **normal**: normal
        # - **online**: online
        self.dts_bis_label = dts_bis_label
        # The ID of the data migration, data synchronization, or change tracking instance.
        # > Separate multiple instance IDs with commas (,). Make sure that the **JobType** parameter is set as expected.
        self.dts_instance_id = dts_instance_id
        # The ID of the data migration, data synchronization, or change tracking task.
        # 
        # > Separate multiple task IDs with commas (,). Make sure that the **JobType** parameter is set as expected.
        self.dts_job_id = dts_job_id
        # The DTS task ID.
        # > In most cases, you do not need to set this parameter.
        self.group_id = group_id
        # The ID of the source or destination database instance that corresponds to the **InstanceType** request parameter.
        self.instance_id = instance_id
        # The type of the source or destination database instance.
        self.instance_type = instance_type
        # The task type of the DTS instance. Valid values:
        # - **MIGRATION**: data migration (default).
        # - **SYNC**: data synchronization.
        # - **SUBSCRIBE**: change tracking.
        self.job_type = job_type
        # The sort criterion when the response contains multiple DTS instances. Valid values:
        # 
        # - **CreateTime**: sorts by task creation time.
        # - **FinishTime**: sorts by task completion time.
        # - **duLimit** (dedicated cluster tasks): sorts by the upper limit of DU usage for DTS tasks. This value is supported only for dedicated clusters.
        # 
        # > You can also specify **OrderDirection** to set the sort order to ascending or descending.
        self.order_column = order_column
        # The sort order of instances. Valid values:
        # 
        # - **ASC**: ascending order. This is the default value.
        # - **DESC**: descending order.
        self.order_direction = order_direction
        self.owner_id = owner_id
        # The page number. The value must be a positive integer that does not exceed the maximum value of the Integer data type. Default value: **1**.
        self.page_number = page_number
        # The number of records per page. Valid values: **10**, **20**, and **30**. Default value: **20**. Maximum value: **30**.
        self.page_size = page_size
        # The specific content of the query condition.
        # > Specify **Type** in advance to define the query condition.
        self.params = params
        # The region in which the DTS instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region = region
        # Deprecated parameter.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of the destination database instance.
        self.src_product_type = src_product_type
        # The instance status of the DTS instance. Valid values:
        # 
        # Data migration task statuses:
        # - **NotStarted**: not started.
        # - **Prechecking**: running a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **NotConfigured**: not configured.
        # - **Migrating**: migrating.
        # - **Suspending**: paused.
        # - **MigrationFailed**: migration failed.
        # - **Finished**: completed.
        # - **Retrying**: retrying.
        # - **Upgrade**: upgrading.
        # - **Locked**: locked.
        # - **Downgrade**: downgrading.
        # 
        # Data synchronization task statuses:
        # - **NotStarted**: not started.
        # - **Prechecking**: running a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **NotConfigured**: not configured.
        # - **Initializing**: performing initial synchronization.
        # - **InitializeFailed**: initial synchronization failed.
        # - **Synchronizing**: synchronizing.
        # - **Failed**: synchronization failed.
        # - **Suspending**: paused.
        # - **Modifying**: modifying synchronization objects.
        # - **Finished**: completed.
        # - **Retrying**: retrying.
        # - **Upgrade**: upgrading.
        # - **Locked**: locked.
        # - **Downgrade**: downgrading.
        # 
        # Change tracking task statuses:
        # - **NotConfigured**: not configured.
        # - **NotStarted**: not started.
        # - **Prechecking**: running a precheck.
        # - **PrecheckFailed**: precheck failed.
        # - **PreCheckPass**: precheck passed.
        # - **Starting**: starting.
        # - **Normal**: normal.
        # - **Retrying**: retrying.
        # - **Abnormal**: abnormal.
        # - **Upgrade**: upgrading.
        # - **Locked**: locked.
        # - **Downgrade**: downgrading.
        self.status = status
        # The tag-based search condition in JSON format.
        # > You can call the **ListTagResources** operation to query tag keys and values.
        self.tags = tags
        # The conditional query parameter. Valid values:
        # 
        # - **instance**: queries by DTS instance ID.
        # - **name**: queries by DTS instance name. Fuzzy match is supported.
        # - **srcRds**: queries by the ID of the source instance (ApsaraDB RDS).
        # - **rds**: queries by the ID of the destination instance (ApsaraDB RDS).
        # 
        # > Specify the **Params** parameter to provide the specific content of the query condition.
        self.type = type
        # Specifies whether to exclude task objects from the response (not return the **DbObject** parameter). Valid values:
        # 
        # - **true**: excludes **DbObject** from the response.
        # - **false**: includes **DbObject** in the response, which can improve the response speed.
        self.without_db_list = without_db_list
        # Specifies whether the node is a seamless integration (Zero-ETL) node. Valid values:
        # 
        # - **false**: No.
        # - **true**: Yes.
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

