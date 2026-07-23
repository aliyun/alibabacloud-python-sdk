# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms20250414 import models as main_models
from darabonba.model import DaraModel

class AgenticDmsInstanceSyncTaskInstance(DaraModel):
    def __init__(
        self,
        catalog_uuid: str = None,
        crawler_task_id: str = None,
        datasource_uuid: str = None,
        db_type: str = None,
        dms_instance_id: str = None,
        dms_instance_summary: main_models.AgenticDmsInstanceSyncTaskInstanceDmsInstanceSummary = None,
        dms_region_id: str = None,
        error_code: str = None,
        error_summary: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        phase: str = None,
        status: str = None,
    ):
        self.catalog_uuid = catalog_uuid
        self.crawler_task_id = crawler_task_id
        self.datasource_uuid = datasource_uuid
        self.db_type = db_type
        self.dms_instance_id = dms_instance_id
        self.dms_instance_summary = dms_instance_summary
        self.dms_region_id = dms_region_id
        self.error_code = error_code
        self.error_summary = error_summary
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.phase = phase
        self.status = status

    def validate(self):
        if self.dms_instance_summary:
            self.dms_instance_summary.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog_uuid is not None:
            result['CatalogUuid'] = self.catalog_uuid

        if self.crawler_task_id is not None:
            result['CrawlerTaskId'] = self.crawler_task_id

        if self.datasource_uuid is not None:
            result['DatasourceUuid'] = self.datasource_uuid

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dms_instance_id is not None:
            result['DmsInstanceId'] = self.dms_instance_id

        if self.dms_instance_summary is not None:
            result['DmsInstanceSummary'] = self.dms_instance_summary.to_map()

        if self.dms_region_id is not None:
            result['DmsRegionId'] = self.dms_region_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_summary is not None:
            result['ErrorSummary'] = self.error_summary

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CatalogUuid') is not None:
            self.catalog_uuid = m.get('CatalogUuid')

        if m.get('CrawlerTaskId') is not None:
            self.crawler_task_id = m.get('CrawlerTaskId')

        if m.get('DatasourceUuid') is not None:
            self.datasource_uuid = m.get('DatasourceUuid')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DmsInstanceId') is not None:
            self.dms_instance_id = m.get('DmsInstanceId')

        if m.get('DmsInstanceSummary') is not None:
            temp_model = main_models.AgenticDmsInstanceSyncTaskInstanceDmsInstanceSummary()
            self.dms_instance_summary = temp_model.from_map(m.get('DmsInstanceSummary'))

        if m.get('DmsRegionId') is not None:
            self.dms_region_id = m.get('DmsRegionId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorSummary') is not None:
            self.error_summary = m.get('ErrorSummary')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self



class AgenticDmsInstanceSyncTaskInstanceDmsInstanceSummary(DaraModel):
    def __init__(
        self,
        alias: str = None,
        db_type: str = None,
        env_type: str = None,
        host: str = None,
        instance_resource_id: str = None,
        instance_source: str = None,
        port: int = None,
        region_id: str = None,
    ):
        self.alias = alias
        self.db_type = db_type
        self.env_type = env_type
        self.host = host
        self.instance_resource_id = instance_resource_id
        self.instance_source = instance_source
        self.port = port
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_resource_id is not None:
            result['InstanceResourceId'] = self.instance_resource_id

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.port is not None:
            result['Port'] = self.port

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceResourceId') is not None:
            self.instance_resource_id = m.get('InstanceResourceId')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

