# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class DsgSceneAddOrUpdateSceneRequest(DaraModel):
    def __init__(
        self,
        scenes: List[main_models.DsgSceneAddOrUpdateSceneRequestScenes] = None,
    ):
        # The information about the level-2 data masking scenario.
        # 
        # This parameter is required.
        self.scenes = scenes

    def validate(self):
        if self.scenes:
            for v1 in self.scenes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['scenes'] = []
        if self.scenes is not None:
            for k1 in self.scenes:
                result['scenes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scenes = []
        if m.get('scenes') is not None:
            for k1 in m.get('scenes'):
                temp_model = main_models.DsgSceneAddOrUpdateSceneRequestScenes()
                self.scenes.append(temp_model.from_map(k1))

        return self

class DsgSceneAddOrUpdateSceneRequestScenes(DaraModel):
    def __init__(
        self,
        desc: str = None,
        id: str = None,
        projects: List[main_models.DsgSceneAddOrUpdateSceneRequestScenesProjects] = None,
        scene_code: str = None,
        scene_name: str = None,
        user_group_ids: List[int] = None,
    ):
        # The description.
        self.desc = desc
        # The ID of the level-2 data masking scenario.
        # 
        # *   If you do not configure this parameter, the current operation is to add a level-2 data masking scenario.
        # *   If you configure this parameter, the current operation is to modify a level-2 data masking scenario. You can call the [DsgSceneQuerySceneListByName](https://help.aliyun.com/document_detail/2786322.html) operation to query the ID of the level-2 data masking scenario.
        self.id = id
        # The information about the compute engine for which the data masking scenario takes effect.
        self.projects = projects
        # The code of the level-1 data masking scenario to which the level-2 data masking scenario belongs. Valid values:
        # 
        # *   dataworks_display_desense_code: masking of displayed data in DataStudio and Data Map
        # *   maxcompute_desense_code: data masking at the MaxCompute compute engine layer
        # *   maxcompute_new_desense_code: data masking at the MaxCompute compute engine layer (new)
        # *   dataworks_analysis_desense_code: masking of displayed data in DataAnalysis
        # 
        # This parameter is required.
        self.scene_code = scene_code
        # The name of the level-2 data masking scenario.
        # 
        # This parameter is required.
        self.scene_name = scene_name
        # The information about the user group for which the data masking scenario takes effect.
        self.user_group_ids = user_group_ids

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
        if self.desc is not None:
            result['desc'] = self.desc

        if self.id is not None:
            result['id'] = self.id

        result['projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['projects'].append(k1.to_map() if k1 else None)

        if self.scene_code is not None:
            result['sceneCode'] = self.scene_code

        if self.scene_name is not None:
            result['sceneName'] = self.scene_name

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('id') is not None:
            self.id = m.get('id')

        self.projects = []
        if m.get('projects') is not None:
            for k1 in m.get('projects'):
                temp_model = main_models.DsgSceneAddOrUpdateSceneRequestScenesProjects()
                self.projects.append(temp_model.from_map(k1))

        if m.get('sceneCode') is not None:
            self.scene_code = m.get('sceneCode')

        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        return self

class DsgSceneAddOrUpdateSceneRequestScenesProjects(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        db_type: str = None,
        project_name: str = None,
    ):
        # If the data masking scenario takes effect for an E-MapReduce (EMR) compute engine, enter the ID of an EMR cluster. This parameter is required only when you use an EMR compute engine.
        self.cluster_id = cluster_id
        # The type of the compute engine for which the data masking scenario takes effect. Valid values:
        # 
        # *   ODPS: ODPS.ODPS
        # *   HOLO: HOLO.POSTGRES
        # *   EMR: EMR
        self.db_type = db_type
        # The name of the compute engine instance for which the data masking scenario takes effect.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id

        if self.db_type is not None:
            result['dbType'] = self.db_type

        if self.project_name is not None:
            result['projectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')

        if m.get('dbType') is not None:
            self.db_type = m.get('dbType')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        return self

