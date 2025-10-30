# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeHadoopConfigsRequest(DaraModel):
    def __init__(
        self,
        config_name: str = None,
        dbinstance_id: str = None,
        emr_instance_id: str = None,
        region_id: str = None,
    ):
        # The name of the configuration file. Valid values:
        # 
        # *   hdfs-site
        # *   core-site
        # *   yarn-site
        # *   mapred-site
        # *   hive-site
        # 
        # This parameter is required.
        self.config_name = config_name
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The E-MapReduce (EMR) Hadoop cluster ID.
        # 
        # This parameter is required.
        self.emr_instance_id = emr_instance_id
        # The region ID of the instance.
        # 
        # >  You can call the [DescribeRegions](https://help.aliyun.com/document_detail/86912.html) operation to query the most recent region list.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_name is not None:
            result['ConfigName'] = self.config_name

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.emr_instance_id is not None:
            result['EmrInstanceId'] = self.emr_instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigName') is not None:
            self.config_name = m.get('ConfigName')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('EmrInstanceId') is not None:
            self.emr_instance_id = m.get('EmrInstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

