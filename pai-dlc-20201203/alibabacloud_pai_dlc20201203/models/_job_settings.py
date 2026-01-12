# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class JobSettings(DaraModel):
    def __init__(
        self,
        advanced_settings: Dict[str, Any] = None,
        allocate_all_rdmadevices: bool = None,
        business_user_id: str = None,
        caller: str = None,
        data_juicer_config: main_models.DataJuicerConfig = None,
        disable_ecs_stock_check: bool = None,
        driver: str = None,
        enable_cpuaffinity: bool = None,
        enable_dswdev: bool = None,
        enable_error_monitoring_in_aimaster: bool = None,
        enable_oss_append: bool = None,
        enable_rdma: bool = None,
        enable_sanity_check: bool = None,
        enable_tide_resource: bool = None,
        error_monitoring_args: str = None,
        job_reserved_minutes: int = None,
        job_reserved_policy: str = None,
        model_config: main_models.ModelConfig = None,
        oversold_type: str = None,
        pipeline_id: str = None,
        sanity_check_args: str = None,
        tags: Dict[str, str] = None,
    ):
        self.advanced_settings = advanced_settings
        self.allocate_all_rdmadevices = allocate_all_rdmadevices
        self.business_user_id = business_user_id
        self.caller = caller
        self.data_juicer_config = data_juicer_config
        self.disable_ecs_stock_check = disable_ecs_stock_check
        self.driver = driver
        self.enable_cpuaffinity = enable_cpuaffinity
        self.enable_dswdev = enable_dswdev
        self.enable_error_monitoring_in_aimaster = enable_error_monitoring_in_aimaster
        self.enable_oss_append = enable_oss_append
        self.enable_rdma = enable_rdma
        self.enable_sanity_check = enable_sanity_check
        self.enable_tide_resource = enable_tide_resource
        self.error_monitoring_args = error_monitoring_args
        self.job_reserved_minutes = job_reserved_minutes
        self.job_reserved_policy = job_reserved_policy
        self.model_config = model_config
        self.oversold_type = oversold_type
        self.pipeline_id = pipeline_id
        self.sanity_check_args = sanity_check_args
        self.tags = tags

    def validate(self):
        if self.data_juicer_config:
            self.data_juicer_config.validate()
        if self.model_config:
            self.model_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.advanced_settings is not None:
            result['AdvancedSettings'] = self.advanced_settings

        if self.allocate_all_rdmadevices is not None:
            result['AllocateAllRDMADevices'] = self.allocate_all_rdmadevices

        if self.business_user_id is not None:
            result['BusinessUserId'] = self.business_user_id

        if self.caller is not None:
            result['Caller'] = self.caller

        if self.data_juicer_config is not None:
            result['DataJuicerConfig'] = self.data_juicer_config.to_map()

        if self.disable_ecs_stock_check is not None:
            result['DisableEcsStockCheck'] = self.disable_ecs_stock_check

        if self.driver is not None:
            result['Driver'] = self.driver

        if self.enable_cpuaffinity is not None:
            result['EnableCPUAffinity'] = self.enable_cpuaffinity

        if self.enable_dswdev is not None:
            result['EnableDSWDev'] = self.enable_dswdev

        if self.enable_error_monitoring_in_aimaster is not None:
            result['EnableErrorMonitoringInAIMaster'] = self.enable_error_monitoring_in_aimaster

        if self.enable_oss_append is not None:
            result['EnableOssAppend'] = self.enable_oss_append

        if self.enable_rdma is not None:
            result['EnableRDMA'] = self.enable_rdma

        if self.enable_sanity_check is not None:
            result['EnableSanityCheck'] = self.enable_sanity_check

        if self.enable_tide_resource is not None:
            result['EnableTideResource'] = self.enable_tide_resource

        if self.error_monitoring_args is not None:
            result['ErrorMonitoringArgs'] = self.error_monitoring_args

        if self.job_reserved_minutes is not None:
            result['JobReservedMinutes'] = self.job_reserved_minutes

        if self.job_reserved_policy is not None:
            result['JobReservedPolicy'] = self.job_reserved_policy

        if self.model_config is not None:
            result['ModelConfig'] = self.model_config.to_map()

        if self.oversold_type is not None:
            result['OversoldType'] = self.oversold_type

        if self.pipeline_id is not None:
            result['PipelineId'] = self.pipeline_id

        if self.sanity_check_args is not None:
            result['SanityCheckArgs'] = self.sanity_check_args

        if self.tags is not None:
            result['Tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdvancedSettings') is not None:
            self.advanced_settings = m.get('AdvancedSettings')

        if m.get('AllocateAllRDMADevices') is not None:
            self.allocate_all_rdmadevices = m.get('AllocateAllRDMADevices')

        if m.get('BusinessUserId') is not None:
            self.business_user_id = m.get('BusinessUserId')

        if m.get('Caller') is not None:
            self.caller = m.get('Caller')

        if m.get('DataJuicerConfig') is not None:
            temp_model = main_models.DataJuicerConfig()
            self.data_juicer_config = temp_model.from_map(m.get('DataJuicerConfig'))

        if m.get('DisableEcsStockCheck') is not None:
            self.disable_ecs_stock_check = m.get('DisableEcsStockCheck')

        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('EnableCPUAffinity') is not None:
            self.enable_cpuaffinity = m.get('EnableCPUAffinity')

        if m.get('EnableDSWDev') is not None:
            self.enable_dswdev = m.get('EnableDSWDev')

        if m.get('EnableErrorMonitoringInAIMaster') is not None:
            self.enable_error_monitoring_in_aimaster = m.get('EnableErrorMonitoringInAIMaster')

        if m.get('EnableOssAppend') is not None:
            self.enable_oss_append = m.get('EnableOssAppend')

        if m.get('EnableRDMA') is not None:
            self.enable_rdma = m.get('EnableRDMA')

        if m.get('EnableSanityCheck') is not None:
            self.enable_sanity_check = m.get('EnableSanityCheck')

        if m.get('EnableTideResource') is not None:
            self.enable_tide_resource = m.get('EnableTideResource')

        if m.get('ErrorMonitoringArgs') is not None:
            self.error_monitoring_args = m.get('ErrorMonitoringArgs')

        if m.get('JobReservedMinutes') is not None:
            self.job_reserved_minutes = m.get('JobReservedMinutes')

        if m.get('JobReservedPolicy') is not None:
            self.job_reserved_policy = m.get('JobReservedPolicy')

        if m.get('ModelConfig') is not None:
            temp_model = main_models.ModelConfig()
            self.model_config = temp_model.from_map(m.get('ModelConfig'))

        if m.get('OversoldType') is not None:
            self.oversold_type = m.get('OversoldType')

        if m.get('PipelineId') is not None:
            self.pipeline_id = m.get('PipelineId')

        if m.get('SanityCheckArgs') is not None:
            self.sanity_check_args = m.get('SanityCheckArgs')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        return self

