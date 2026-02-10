# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeFieldStatisticsResponseBody(DaraModel):
    def __init__(
        self,
        grouped_fields: main_models.DescribeFieldStatisticsResponseBodyGroupedFields = None,
        request_id: str = None,
    ):
        # The information about servers that are returned.
        self.grouped_fields = grouped_fields
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.grouped_fields:
            self.grouped_fields.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.grouped_fields is not None:
            result['GroupedFields'] = self.grouped_fields.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupedFields') is not None:
            temp_model = main_models.DescribeFieldStatisticsResponseBodyGroupedFields()
            self.grouped_fields = temp_model.from_map(m.get('GroupedFields'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeFieldStatisticsResponseBodyGroupedFields(DaraModel):
    def __init__(
        self,
        ali_yun_instance_count: int = None,
        aws_instance_count: int = None,
        azure_instance_count: int = None,
        exposed_instance_core_count: int = None,
        exposed_instance_count: int = None,
        general_asset_count: int = None,
        google_instance_count: int = None,
        group_count: int = None,
        huawei_instance_count: int = None,
        idc_instance_count: int = None,
        important_asset_count: int = None,
        instance_core_count: int = None,
        instance_count: int = None,
        instance_sync_task_count: int = None,
        new_instance_core_count: int = None,
        new_instance_count: int = None,
        no_risk_instance_count: int = None,
        not_bind_machine_instance_count: int = None,
        not_running_status_core_count: int = None,
        not_running_status_count: int = None,
        offline_instance_count: int = None,
        out_machine_instance_count: int = None,
        pause_instance_count: int = None,
        region_count: int = None,
        risk_instance_core_count: int = None,
        risk_instance_count: int = None,
        tencent_instance_count: int = None,
        test_asset_count: int = None,
        tripartite_instance_count: int = None,
        un_know_status_instance_count: int = None,
        unprotected_instance_core_count: int = None,
        unprotected_instance_count: int = None,
        volcengine_instance_count: int = None,
        vpc_count: int = None,
    ):
        # The number of assets that are deployed on Alibaba Cloud.
        self.ali_yun_instance_count = ali_yun_instance_count
        # The number of servers.
        self.aws_instance_count = aws_instance_count
        # The number of third-party cloud servers.
        self.azure_instance_count = azure_instance_count
        # The number of cores of exposed assets.
        self.exposed_instance_core_count = exposed_instance_core_count
        # The number of exposed servers.
        self.exposed_instance_count = exposed_instance_count
        # The number of assets whose importance is common.
        self.general_asset_count = general_asset_count
        # The number of instances that are provisioned by third-party providers.
        self.google_instance_count = google_instance_count
        # The number of server groups.
        self.group_count = group_count
        # The number of instances that are provisioned by third-party providers.
        self.huawei_instance_count = huawei_instance_count
        # The number of assets that can be protected by Security Center.
        self.idc_instance_count = idc_instance_count
        # The number of assets whose importance is important.
        self.important_asset_count = important_asset_count
        # The number of cores of assets in the specified asset type. If the asset type is not specified, the value of this parameter indicates the total number of cores of servers and Alibaba Cloud services within your account.
        self.instance_core_count = instance_core_count
        # The total number of assets of the specified type. If no asset types are specified, this parameter indicates the total number of all servers and Alibaba Cloud services within your account.
        self.instance_count = instance_count
        # The total number of tasks for the specified type of assets. If no asset types are specified, this parameter indicates the total number of all servers and Alibaba Cloud services within your account.
        self.instance_sync_task_count = instance_sync_task_count
        # The number of cores of new servers.
        self.new_instance_core_count = new_instance_core_count
        # The number of newly added servers.
        self.new_instance_count = new_instance_count
        # The number of servers on which no risks are detected.
        self.no_risk_instance_count = no_risk_instance_count
        # The number of assets that are not added to Security Center of the specified asset type.
        self.not_bind_machine_instance_count = not_bind_machine_instance_count
        # The number of cores of servers that are not started.
        self.not_running_status_core_count = not_running_status_core_count
        # The number of servers that are shut down.
        self.not_running_status_count = not_running_status_count
        # The number of servers whose Security Center agent status is Offline.
        self.offline_instance_count = offline_instance_count
        # The number of servers outside the cloud.
        self.out_machine_instance_count = out_machine_instance_count
        # The number of servers for which the Security Center agent suspends protection.
        self.pause_instance_count = pause_instance_count
        # The number of regions to which the servers belong.
        self.region_count = region_count
        # The number of cores of vulnerable assets.
        self.risk_instance_core_count = risk_instance_core_count
        # The number of assets that are at risk.
        self.risk_instance_count = risk_instance_count
        # The total number of cloud services that are protected by Security Center.
        self.tencent_instance_count = tencent_instance_count
        # The number of assets whose importance is test.
        self.test_asset_count = test_asset_count
        # The number of simple application servers.
        self.tripartite_instance_count = tripartite_instance_count
        # The number of servers that are in the Unknown state.
        self.un_know_status_instance_count = un_know_status_instance_count
        # The number of cores of unprotected assets.
        self.unprotected_instance_core_count = unprotected_instance_core_count
        # The number of unprotected assets.
        self.unprotected_instance_count = unprotected_instance_count
        # The number of instances that are provisioned by third-party providers.
        self.volcengine_instance_count = volcengine_instance_count
        # The number of virtual private clouds (VPCs).
        self.vpc_count = vpc_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_yun_instance_count is not None:
            result['AliYunInstanceCount'] = self.ali_yun_instance_count

        if self.aws_instance_count is not None:
            result['AwsInstanceCount'] = self.aws_instance_count

        if self.azure_instance_count is not None:
            result['AzureInstanceCount'] = self.azure_instance_count

        if self.exposed_instance_core_count is not None:
            result['ExposedInstanceCoreCount'] = self.exposed_instance_core_count

        if self.exposed_instance_count is not None:
            result['ExposedInstanceCount'] = self.exposed_instance_count

        if self.general_asset_count is not None:
            result['GeneralAssetCount'] = self.general_asset_count

        if self.google_instance_count is not None:
            result['GoogleInstanceCount'] = self.google_instance_count

        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.huawei_instance_count is not None:
            result['HuaweiInstanceCount'] = self.huawei_instance_count

        if self.idc_instance_count is not None:
            result['IdcInstanceCount'] = self.idc_instance_count

        if self.important_asset_count is not None:
            result['ImportantAssetCount'] = self.important_asset_count

        if self.instance_core_count is not None:
            result['InstanceCoreCount'] = self.instance_core_count

        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count

        if self.instance_sync_task_count is not None:
            result['InstanceSyncTaskCount'] = self.instance_sync_task_count

        if self.new_instance_core_count is not None:
            result['NewInstanceCoreCount'] = self.new_instance_core_count

        if self.new_instance_count is not None:
            result['NewInstanceCount'] = self.new_instance_count

        if self.no_risk_instance_count is not None:
            result['NoRiskInstanceCount'] = self.no_risk_instance_count

        if self.not_bind_machine_instance_count is not None:
            result['NotBindMachineInstanceCount'] = self.not_bind_machine_instance_count

        if self.not_running_status_core_count is not None:
            result['NotRunningStatusCoreCount'] = self.not_running_status_core_count

        if self.not_running_status_count is not None:
            result['NotRunningStatusCount'] = self.not_running_status_count

        if self.offline_instance_count is not None:
            result['OfflineInstanceCount'] = self.offline_instance_count

        if self.out_machine_instance_count is not None:
            result['OutMachineInstanceCount'] = self.out_machine_instance_count

        if self.pause_instance_count is not None:
            result['PauseInstanceCount'] = self.pause_instance_count

        if self.region_count is not None:
            result['RegionCount'] = self.region_count

        if self.risk_instance_core_count is not None:
            result['RiskInstanceCoreCount'] = self.risk_instance_core_count

        if self.risk_instance_count is not None:
            result['RiskInstanceCount'] = self.risk_instance_count

        if self.tencent_instance_count is not None:
            result['TencentInstanceCount'] = self.tencent_instance_count

        if self.test_asset_count is not None:
            result['TestAssetCount'] = self.test_asset_count

        if self.tripartite_instance_count is not None:
            result['TripartiteInstanceCount'] = self.tripartite_instance_count

        if self.un_know_status_instance_count is not None:
            result['UnKnowStatusInstanceCount'] = self.un_know_status_instance_count

        if self.unprotected_instance_core_count is not None:
            result['UnprotectedInstanceCoreCount'] = self.unprotected_instance_core_count

        if self.unprotected_instance_count is not None:
            result['UnprotectedInstanceCount'] = self.unprotected_instance_count

        if self.volcengine_instance_count is not None:
            result['VolcengineInstanceCount'] = self.volcengine_instance_count

        if self.vpc_count is not None:
            result['VpcCount'] = self.vpc_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliYunInstanceCount') is not None:
            self.ali_yun_instance_count = m.get('AliYunInstanceCount')

        if m.get('AwsInstanceCount') is not None:
            self.aws_instance_count = m.get('AwsInstanceCount')

        if m.get('AzureInstanceCount') is not None:
            self.azure_instance_count = m.get('AzureInstanceCount')

        if m.get('ExposedInstanceCoreCount') is not None:
            self.exposed_instance_core_count = m.get('ExposedInstanceCoreCount')

        if m.get('ExposedInstanceCount') is not None:
            self.exposed_instance_count = m.get('ExposedInstanceCount')

        if m.get('GeneralAssetCount') is not None:
            self.general_asset_count = m.get('GeneralAssetCount')

        if m.get('GoogleInstanceCount') is not None:
            self.google_instance_count = m.get('GoogleInstanceCount')

        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('HuaweiInstanceCount') is not None:
            self.huawei_instance_count = m.get('HuaweiInstanceCount')

        if m.get('IdcInstanceCount') is not None:
            self.idc_instance_count = m.get('IdcInstanceCount')

        if m.get('ImportantAssetCount') is not None:
            self.important_asset_count = m.get('ImportantAssetCount')

        if m.get('InstanceCoreCount') is not None:
            self.instance_core_count = m.get('InstanceCoreCount')

        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')

        if m.get('InstanceSyncTaskCount') is not None:
            self.instance_sync_task_count = m.get('InstanceSyncTaskCount')

        if m.get('NewInstanceCoreCount') is not None:
            self.new_instance_core_count = m.get('NewInstanceCoreCount')

        if m.get('NewInstanceCount') is not None:
            self.new_instance_count = m.get('NewInstanceCount')

        if m.get('NoRiskInstanceCount') is not None:
            self.no_risk_instance_count = m.get('NoRiskInstanceCount')

        if m.get('NotBindMachineInstanceCount') is not None:
            self.not_bind_machine_instance_count = m.get('NotBindMachineInstanceCount')

        if m.get('NotRunningStatusCoreCount') is not None:
            self.not_running_status_core_count = m.get('NotRunningStatusCoreCount')

        if m.get('NotRunningStatusCount') is not None:
            self.not_running_status_count = m.get('NotRunningStatusCount')

        if m.get('OfflineInstanceCount') is not None:
            self.offline_instance_count = m.get('OfflineInstanceCount')

        if m.get('OutMachineInstanceCount') is not None:
            self.out_machine_instance_count = m.get('OutMachineInstanceCount')

        if m.get('PauseInstanceCount') is not None:
            self.pause_instance_count = m.get('PauseInstanceCount')

        if m.get('RegionCount') is not None:
            self.region_count = m.get('RegionCount')

        if m.get('RiskInstanceCoreCount') is not None:
            self.risk_instance_core_count = m.get('RiskInstanceCoreCount')

        if m.get('RiskInstanceCount') is not None:
            self.risk_instance_count = m.get('RiskInstanceCount')

        if m.get('TencentInstanceCount') is not None:
            self.tencent_instance_count = m.get('TencentInstanceCount')

        if m.get('TestAssetCount') is not None:
            self.test_asset_count = m.get('TestAssetCount')

        if m.get('TripartiteInstanceCount') is not None:
            self.tripartite_instance_count = m.get('TripartiteInstanceCount')

        if m.get('UnKnowStatusInstanceCount') is not None:
            self.un_know_status_instance_count = m.get('UnKnowStatusInstanceCount')

        if m.get('UnprotectedInstanceCoreCount') is not None:
            self.unprotected_instance_core_count = m.get('UnprotectedInstanceCoreCount')

        if m.get('UnprotectedInstanceCount') is not None:
            self.unprotected_instance_count = m.get('UnprotectedInstanceCount')

        if m.get('VolcengineInstanceCount') is not None:
            self.volcengine_instance_count = m.get('VolcengineInstanceCount')

        if m.get('VpcCount') is not None:
            self.vpc_count = m.get('VpcCount')

        return self

