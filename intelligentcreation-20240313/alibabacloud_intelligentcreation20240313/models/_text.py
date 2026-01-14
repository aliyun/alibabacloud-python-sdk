# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class Text(DaraModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_name: str = None,
        desc: str = None,
        err_msg: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        illustration_task_id_list: List[int] = None,
        publish_status: str = None,
        text_content: str = None,
        text_id: int = None,
        text_illustration_tag: bool = None,
        text_mode_type: str = None,
        text_status: str = None,
        text_style_type: str = None,
        text_task_id: int = None,
        text_themes: List[str] = None,
        title: str = None,
        user_name_create: str = None,
        user_name_modified: str = None,
    ):
        self.agent_id = agent_id
        self.agent_name = agent_name
        # This parameter is required.
        self.desc = desc
        self.err_msg = err_msg
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.illustration_task_id_list = illustration_task_id_list
        self.publish_status = publish_status
        self.text_content = text_content
        # This parameter is required.
        self.text_id = text_id
        self.text_illustration_tag = text_illustration_tag
        self.text_mode_type = text_mode_type
        # This parameter is required.
        self.text_status = text_status
        self.text_style_type = text_style_type
        # This parameter is required.
        self.text_task_id = text_task_id
        self.text_themes = text_themes
        self.title = title
        # This parameter is required.
        self.user_name_create = user_name_create
        # This parameter is required.
        self.user_name_modified = user_name_modified

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_id is not None:
            result['agentId'] = self.agent_id

        if self.agent_name is not None:
            result['agentName'] = self.agent_name

        if self.desc is not None:
            result['desc'] = self.desc

        if self.err_msg is not None:
            result['errMsg'] = self.err_msg

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.illustration_task_id_list is not None:
            result['illustrationTaskIdList'] = self.illustration_task_id_list

        if self.publish_status is not None:
            result['publishStatus'] = self.publish_status

        if self.text_content is not None:
            result['textContent'] = self.text_content

        if self.text_id is not None:
            result['textId'] = self.text_id

        if self.text_illustration_tag is not None:
            result['textIllustrationTag'] = self.text_illustration_tag

        if self.text_mode_type is not None:
            result['textModeType'] = self.text_mode_type

        if self.text_status is not None:
            result['textStatus'] = self.text_status

        if self.text_style_type is not None:
            result['textStyleType'] = self.text_style_type

        if self.text_task_id is not None:
            result['textTaskId'] = self.text_task_id

        if self.text_themes is not None:
            result['textThemes'] = self.text_themes

        if self.title is not None:
            result['title'] = self.title

        if self.user_name_create is not None:
            result['userNameCreate'] = self.user_name_create

        if self.user_name_modified is not None:
            result['userNameModified'] = self.user_name_modified

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')

        if m.get('agentName') is not None:
            self.agent_name = m.get('agentName')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('errMsg') is not None:
            self.err_msg = m.get('errMsg')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('illustrationTaskIdList') is not None:
            self.illustration_task_id_list = m.get('illustrationTaskIdList')

        if m.get('publishStatus') is not None:
            self.publish_status = m.get('publishStatus')

        if m.get('textContent') is not None:
            self.text_content = m.get('textContent')

        if m.get('textId') is not None:
            self.text_id = m.get('textId')

        if m.get('textIllustrationTag') is not None:
            self.text_illustration_tag = m.get('textIllustrationTag')

        if m.get('textModeType') is not None:
            self.text_mode_type = m.get('textModeType')

        if m.get('textStatus') is not None:
            self.text_status = m.get('textStatus')

        if m.get('textStyleType') is not None:
            self.text_style_type = m.get('textStyleType')

        if m.get('textTaskId') is not None:
            self.text_task_id = m.get('textTaskId')

        if m.get('textThemes') is not None:
            self.text_themes = m.get('textThemes')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('userNameCreate') is not None:
            self.user_name_create = m.get('userNameCreate')

        if m.get('userNameModified') is not None:
            self.user_name_modified = m.get('userNameModified')

        return self

