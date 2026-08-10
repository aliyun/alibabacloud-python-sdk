# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ExecuteDDLRequest(DaraModel):
    def __init__(
        self,
        context: main_models.ExecuteDDLRequestContext = None,
        ddlcommand: main_models.ExecuteDDLRequestDDLCommand = None,
        op_tenant_id: int = None,
    ):
        # The request context information.
        # 
        # This parameter is required.
        self.context = context
        # The one-click table creation parameters.
        # 
        # This parameter is required.
        self.ddlcommand = ddlcommand
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.context:
            self.context.validate()
        if self.ddlcommand:
            self.ddlcommand.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context is not None:
            result['Context'] = self.context.to_map()

        if self.ddlcommand is not None:
            result['DDLCommand'] = self.ddlcommand.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Context') is not None:
            temp_model = main_models.ExecuteDDLRequestContext()
            self.context = temp_model.from_map(m.get('Context'))

        if m.get('DDLCommand') is not None:
            temp_model = main_models.ExecuteDDLRequestDDLCommand()
            self.ddlcommand = temp_model.from_map(m.get('DDLCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class ExecuteDDLRequestDDLCommand(DaraModel):
    def __init__(
        self,
        datasource_id: main_models.ExecuteDDLRequestDDLCommandDatasourceId = None,
        ddl: str = None,
        drop_table: bool = None,
    ):
        # The identifier of the data source, compute source, or dataset used for table creation.
        # 
        # This parameter is required.
        self.datasource_id = datasource_id
        # The DDL statement for table creation.
        # 
        # This parameter is required.
        self.ddl = ddl
        # Specifies whether to drop the table if it already exists.
        self.drop_table = drop_table

    def validate(self):
        if self.datasource_id:
            self.datasource_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_id is not None:
            result['DatasourceId'] = self.datasource_id.to_map()

        if self.ddl is not None:
            result['Ddl'] = self.ddl

        if self.drop_table is not None:
            result['DropTable'] = self.drop_table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceId') is not None:
            temp_model = main_models.ExecuteDDLRequestDDLCommandDatasourceId()
            self.datasource_id = temp_model.from_map(m.get('DatasourceId'))

        if m.get('Ddl') is not None:
            self.ddl = m.get('Ddl')

        if m.get('DropTable') is not None:
            self.drop_table = m.get('DropTable')

        return self

class ExecuteDDLRequestDDLCommandDatasourceId(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        ds_category: str = None,
        ds_id: str = None,
        env: str = None,
        one_catalog_type: str = None,
        project_id: int = None,
        version: str = None,
    ):
        # The catalog of the data source or compute cluster. This parameter is required only in OneCatalog scenarios.
        self.catalog = catalog
        # The data source category. Valid values:
        # 
        # - DATA_SOURCE: physical data source.
        # - PROJECT_COMPUTE_SOURCE: compute source bound to a project.
        # - ONE_CATALOG: compute source or data source in multi-engine mode (OneCatalog).
        # - DATA_SET: dataset.
        # 
        # This parameter is optional. The system automatically infers the category based on other fields if this parameter is not specified.
        self.ds_category = ds_category
        # The ID of the data source, compute source, or dataset. This parameter is optional when DsCategory is set to PROJECT_COMPUTE_SOURCE.
        self.ds_id = ds_id
        # The environment. Valid values:
        # 
        # - DEV: development environment.
        # - PROD: production environment.
        self.env = env
        # The catalog type when DsCategory is set to ONE_CATALOG. Valid values:
        # 
        # - COMPUTE_CLUSTER: compute cluster.
        # - DATA_SOURCE: physical data source.
        self.one_catalog_type = one_catalog_type
        # The ID of the project bound to the compute source. This parameter is required only when DsCategory is set to PROJECT_COMPUTE_SOURCE.
        self.project_id = project_id
        # The dataset version. This parameter is required only when DsCategory is set to DATA_SET.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.ds_category is not None:
            result['DsCategory'] = self.ds_category

        if self.ds_id is not None:
            result['DsId'] = self.ds_id

        if self.env is not None:
            result['Env'] = self.env

        if self.one_catalog_type is not None:
            result['OneCatalogType'] = self.one_catalog_type

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('DsCategory') is not None:
            self.ds_category = m.get('DsCategory')

        if m.get('DsId') is not None:
            self.ds_id = m.get('DsId')

        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('OneCatalogType') is not None:
            self.one_catalog_type = m.get('OneCatalogType')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class ExecuteDDLRequestContext(DaraModel):
    def __init__(
        self,
        env: str = None,
        project_id: int = None,
    ):
        # The current operating environment. Valid values:
        # 
        # - DEV: development environment.
        # - PROD: production environment.
        # 
        # This parameter is required.
        self.env = env
        # The ID of the project to which the integration pipeline task belongs.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env is not None:
            result['Env'] = self.env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Env') is not None:
            self.env = m.get('Env')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

