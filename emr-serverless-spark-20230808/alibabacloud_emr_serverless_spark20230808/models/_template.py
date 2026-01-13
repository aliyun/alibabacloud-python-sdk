# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class Template(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        creator: int = None,
        display_spark_version: str = None,
        fusion: bool = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        is_default: bool = None,
        modifier: int = None,
        name: str = None,
        spark_conf: List[main_models.SparkConf] = None,
        spark_driver_cores: int = None,
        spark_driver_memory: int = None,
        spark_executor_cores: int = None,
        spark_executor_memory: int = None,
        spark_log_level: str = None,
        spark_log_path: str = None,
        spark_version: str = None,
        template_type: str = None,
    ):
        self.biz_id = biz_id
        # This parameter is required.
        self.creator = creator
        self.display_spark_version = display_spark_version
        self.fusion = fusion
        # This parameter is required.
        self.gmt_created = gmt_created
        # This parameter is required.
        self.gmt_modified = gmt_modified
        self.is_default = is_default
        # This parameter is required.
        self.modifier = modifier
        self.name = name
        self.spark_conf = spark_conf
        # This parameter is required.
        self.spark_driver_cores = spark_driver_cores
        # This parameter is required.
        self.spark_driver_memory = spark_driver_memory
        # This parameter is required.
        self.spark_executor_cores = spark_executor_cores
        # This parameter is required.
        self.spark_executor_memory = spark_executor_memory
        # This parameter is required.
        self.spark_log_level = spark_log_level
        # This parameter is required.
        self.spark_log_path = spark_log_path
        # This parameter is required.
        self.spark_version = spark_version
        self.template_type = template_type

    def validate(self):
        if self.spark_conf:
            for v1 in self.spark_conf:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.creator is not None:
            result['creator'] = self.creator

        if self.display_spark_version is not None:
            result['displaySparkVersion'] = self.display_spark_version

        if self.fusion is not None:
            result['fusion'] = self.fusion

        if self.gmt_created is not None:
            result['gmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.is_default is not None:
            result['isDefault'] = self.is_default

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.name is not None:
            result['name'] = self.name

        result['sparkConf'] = []
        if self.spark_conf is not None:
            for k1 in self.spark_conf:
                result['sparkConf'].append(k1.to_map() if k1 else None)

        if self.spark_driver_cores is not None:
            result['sparkDriverCores'] = self.spark_driver_cores

        if self.spark_driver_memory is not None:
            result['sparkDriverMemory'] = self.spark_driver_memory

        if self.spark_executor_cores is not None:
            result['sparkExecutorCores'] = self.spark_executor_cores

        if self.spark_executor_memory is not None:
            result['sparkExecutorMemory'] = self.spark_executor_memory

        if self.spark_log_level is not None:
            result['sparkLogLevel'] = self.spark_log_level

        if self.spark_log_path is not None:
            result['sparkLogPath'] = self.spark_log_path

        if self.spark_version is not None:
            result['sparkVersion'] = self.spark_version

        if self.template_type is not None:
            result['templateType'] = self.template_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('displaySparkVersion') is not None:
            self.display_spark_version = m.get('displaySparkVersion')

        if m.get('fusion') is not None:
            self.fusion = m.get('fusion')

        if m.get('gmtCreated') is not None:
            self.gmt_created = m.get('gmtCreated')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.spark_conf = []
        if m.get('sparkConf') is not None:
            for k1 in m.get('sparkConf'):
                temp_model = main_models.SparkConf()
                self.spark_conf.append(temp_model.from_map(k1))

        if m.get('sparkDriverCores') is not None:
            self.spark_driver_cores = m.get('sparkDriverCores')

        if m.get('sparkDriverMemory') is not None:
            self.spark_driver_memory = m.get('sparkDriverMemory')

        if m.get('sparkExecutorCores') is not None:
            self.spark_executor_cores = m.get('sparkExecutorCores')

        if m.get('sparkExecutorMemory') is not None:
            self.spark_executor_memory = m.get('sparkExecutorMemory')

        if m.get('sparkLogLevel') is not None:
            self.spark_log_level = m.get('sparkLogLevel')

        if m.get('sparkLogPath') is not None:
            self.spark_log_path = m.get('sparkLogPath')

        if m.get('sparkVersion') is not None:
            self.spark_version = m.get('sparkVersion')

        if m.get('templateType') is not None:
            self.template_type = m.get('templateType')

        return self

