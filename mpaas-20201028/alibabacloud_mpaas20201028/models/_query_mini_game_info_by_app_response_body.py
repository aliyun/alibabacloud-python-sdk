# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class QueryMiniGameInfoByAppResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        content: List[main_models.QueryMiniGameInfoByAppResponseBodyContent] = None,
        error_code: str = None,
        request_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.content = content
        self.error_code = error_code
        self.request_id = request_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.content:
            for v1 in self.content:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

        result['Content'] = []
        if self.content is not None:
            for k1 in self.content:
                result['Content'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        self.content = []
        if m.get('Content') is not None:
            for k1 in m.get('Content'):
                temp_model = main_models.QueryMiniGameInfoByAppResponseBodyContent()
                self.content.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryMiniGameInfoByAppResponseBodyContent(DaraModel):
    def __init__(
        self,
        game_engine: str = None,
        game_maker: str = None,
        game_type_level_1: str = None,
        game_type_level_2: str = None,
        game_type_level_3: str = None,
        game_version_id: str = None,
        gmt_modified: int = None,
        icon: str = None,
        introduction: str = None,
        mini_program_code: str = None,
        mini_program_id: int = None,
        mini_program_name: str = None,
        slogan: str = None,
        version: str = None,
    ):
        self.game_engine = game_engine
        self.game_maker = game_maker
        self.game_type_level_1 = game_type_level_1
        self.game_type_level_2 = game_type_level_2
        self.game_type_level_3 = game_type_level_3
        self.game_version_id = game_version_id
        self.gmt_modified = gmt_modified
        self.icon = icon
        self.introduction = introduction
        self.mini_program_code = mini_program_code
        self.mini_program_id = mini_program_id
        self.mini_program_name = mini_program_name
        self.slogan = slogan
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.game_engine is not None:
            result['GameEngine'] = self.game_engine

        if self.game_maker is not None:
            result['GameMaker'] = self.game_maker

        if self.game_type_level_1 is not None:
            result['GameTypeLevel1'] = self.game_type_level_1

        if self.game_type_level_2 is not None:
            result['GameTypeLevel2'] = self.game_type_level_2

        if self.game_type_level_3 is not None:
            result['GameTypeLevel3'] = self.game_type_level_3

        if self.game_version_id is not None:
            result['GameVersionId'] = self.game_version_id

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icon is not None:
            result['Icon'] = self.icon

        if self.introduction is not None:
            result['Introduction'] = self.introduction

        if self.mini_program_code is not None:
            result['MiniProgramCode'] = self.mini_program_code

        if self.mini_program_id is not None:
            result['MiniProgramId'] = self.mini_program_id

        if self.mini_program_name is not None:
            result['MiniProgramName'] = self.mini_program_name

        if self.slogan is not None:
            result['Slogan'] = self.slogan

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GameEngine') is not None:
            self.game_engine = m.get('GameEngine')

        if m.get('GameMaker') is not None:
            self.game_maker = m.get('GameMaker')

        if m.get('GameTypeLevel1') is not None:
            self.game_type_level_1 = m.get('GameTypeLevel1')

        if m.get('GameTypeLevel2') is not None:
            self.game_type_level_2 = m.get('GameTypeLevel2')

        if m.get('GameTypeLevel3') is not None:
            self.game_type_level_3 = m.get('GameTypeLevel3')

        if m.get('GameVersionId') is not None:
            self.game_version_id = m.get('GameVersionId')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Icon') is not None:
            self.icon = m.get('Icon')

        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')

        if m.get('MiniProgramCode') is not None:
            self.mini_program_code = m.get('MiniProgramCode')

        if m.get('MiniProgramId') is not None:
            self.mini_program_id = m.get('MiniProgramId')

        if m.get('MiniProgramName') is not None:
            self.mini_program_name = m.get('MiniProgramName')

        if m.get('Slogan') is not None:
            self.slogan = m.get('Slogan')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

