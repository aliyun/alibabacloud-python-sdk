# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class GetMetaDBInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaDBInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The basic metadata information.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetMetaDBInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetMetaDBInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        app_guid: str = None,
        cluster_biz_id: str = None,
        comment: str = None,
        create_time: int = None,
        endpoint: str = None,
        env_type: int = None,
        location: str = None,
        modify_time: int = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        project_id: int = None,
        project_name: str = None,
        project_name_cn: str = None,
        tenant_id: int = None,
        type: str = None,
    ):
        # The engine ID, in the format of `Engine type.Engine name`.
        self.app_guid = app_guid
        # The EMR cluster ID.
        self.cluster_biz_id = cluster_biz_id
        # The comment.
        self.comment = comment
        # The time when the engine was created.
        # 
        # The value is a 13-digit number, for example, `1541576644000`.
        self.create_time = create_time
        # The service endpoint.
        self.endpoint = endpoint
        # The environment type. A value of 0 indicates a non-production table. A value of 1 indicates a production table.
        self.env_type = env_type
        # The data storage address of the EMR database.
        self.location = location
        # The time when the engine was modified.
        # 
        # The value is a 13-digit number, for example, `1541576644000`.
        self.modify_time = modify_time
        # The database name.
        self.name = name
        # The Alibaba Cloud account ID of the workspace owner.
        self.owner_id = owner_id
        # The name of the workspace owner.
        self.owner_name = owner_name
        # The workspace ID.
        self.project_id = project_id
        # The name of the workspace.
        self.project_name = project_name
        # The display name of the workspace.
        self.project_name_cn = project_name_cn
        # The tenant ID.
        self.tenant_id = tenant_id
        # The database type.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_guid is not None:
            result['AppGuid'] = self.app_guid

        if self.cluster_biz_id is not None:
            result['ClusterBizId'] = self.cluster_biz_id

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.location is not None:
            result['Location'] = self.location

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.project_name_cn is not None:
            result['ProjectNameCn'] = self.project_name_cn

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppGuid') is not None:
            self.app_guid = m.get('AppGuid')

        if m.get('ClusterBizId') is not None:
            self.cluster_biz_id = m.get('ClusterBizId')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('ProjectNameCn') is not None:
            self.project_name_cn = m.get('ProjectNameCn')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

