# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgSceneQuerySceneListByNameResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DsgSceneQuerySceneListByNameResponseBodyData] = None,
        error_code: str = None,
        error_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The returned data.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The request ID. You can locate logs and troubleshoot issues based on the ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DsgSceneQuerySceneListByNameResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DsgSceneQuerySceneListByNameResponseBodyData(DaraModel):
    def __init__(
        self,
        children: List[Any] = None,
        desc: str = None,
        id: int = None,
        projects: List[main_models.DsgSceneQuerySceneListByNameResponseBodyDataProjects] = None,
        scene_code: str = None,
        scene_level: int = None,
        scene_name: str = None,
        user_groups: str = None,
        scence_db_type: str = None,
    ):
        # The information about multiple levels of data masking scenarios.
        self.children = children
        # The description of the data masking scenario.
        self.desc = desc
        # The ID of the data masking scenario.
        self.id = id
        # The information about the compute engine for which the data masking scenario takes effect.
        self.projects = projects
        # The code of the level-1 data masking scenario. Valid values:
        # 
        # *   dataworks_display_desense_code: masking of displayed data in DataStudio and Data Map
        # *   maxcompute_desense_code: data masking at the MaxCompute compute engine layer
        # *   maxcompute_new_desense_code: data masking at the MaxCompute compute engine layer (new)
        # *   hologres_display_desense_code: data masking at the Hologres compute engine layer
        # *   dataworks_data_integration_desense_code: static data masking in Data Integration
        # *   dataworks_analysis_desense_code: masking of displayed data in DataAnalysis
        self.scene_code = scene_code
        # The level of the data masking scenario. Valid values:
        # 
        # *   0: level-1 data masking scenario
        # *   1: level-2 data masking scenario
        self.scene_level = scene_level
        # The name of the data masking scenario.
        self.scene_name = scene_name
        # The list of user groups in the data masking scenario. Separate user groups with commas (,).
        self.user_groups = user_groups
        self.scence_db_type = scence_db_type

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.children is not None:
            result['Children'] = self.children

        if self.desc is not None:
            result['Desc'] = self.desc

        if self.id is not None:
            result['Id'] = self.id

        result['Projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['Projects'].append(k1.to_map() if k1 else None)

        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code

        if self.scene_level is not None:
            result['SceneLevel'] = self.scene_level

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.user_groups is not None:
            result['UserGroups'] = self.user_groups

        if self.scence_db_type is not None:
            result['scenceDbType'] = self.scence_db_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Children') is not None:
            self.children = m.get('Children')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        self.projects = []
        if m.get('Projects') is not None:
            for k1 in m.get('Projects'):
                temp_model = main_models.DsgSceneQuerySceneListByNameResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')

        if m.get('SceneLevel') is not None:
            self.scene_level = m.get('SceneLevel')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('UserGroups') is not None:
            self.user_groups = m.get('UserGroups')

        if m.get('scenceDbType') is not None:
            self.scence_db_type = m.get('scenceDbType')

        return self

class DsgSceneQuerySceneListByNameResponseBodyDataProjects(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_type: str = None,
        project_name: str = None,
    ):
        # The ID of the EMR cluster. This parameter is returned only when the data scope that takes effect in the data masking scenario is an EMR compute engine.
        self.cluster_id = cluster_id
        # The type of the compute engine. Valid values:
        # 
        # *   ODPS: ODPS.ODPS
        # *   HOLO: HOLO.POSTGRES
        # *   EMR: EMR
        self.db_type = db_type
        # The name of the compute engine.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

