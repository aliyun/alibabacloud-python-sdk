# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_workorder20201210 import models as main_models
from darabonba.model import DaraModel

class DialogBaseBody(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.DialogBaseBodyAttachments] = None,
        channel_code: str = None,
        create_time: int = None,
        data_info: main_models.DialogBaseBodyDataInfo = None,
        dialog_id: int = None,
        footer_info: main_models.DialogBaseBodyFooterInfo = None,
        hit_words: List[str] = None,
        modified_time: int = None,
        refer_info: main_models.DialogBaseBody = None,
        stage: int = None,
        status: int = None,
        ticket_id: str = None,
        ticket_status: int = None,
        timestamp: int = None,
        tip: str = None,
        type: int = None,
        user_info: main_models.DialogBaseBodyUserInfo = None,
    ):
        self.attachments = attachments
        self.channel_code = channel_code
        self.create_time = create_time
        self.data_info = data_info
        self.dialog_id = dialog_id
        self.footer_info = footer_info
        self.hit_words = hit_words
        self.modified_time = modified_time
        self.refer_info = refer_info
        self.stage = stage
        self.status = status
        self.ticket_id = ticket_id
        self.ticket_status = ticket_status
        self.timestamp = timestamp
        self.tip = tip
        self.type = type
        self.user_info = user_info

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()
        if self.data_info:
            self.data_info.validate()
        if self.footer_info:
            self.footer_info.validate()
        if self.refer_info:
            self.refer_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        if self.channel_code is not None:
            result['ChannelCode'] = self.channel_code

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.data_info is not None:
            result['DataInfo'] = self.data_info.to_map()

        if self.dialog_id is not None:
            result['DialogId'] = self.dialog_id

        if self.footer_info is not None:
            result['FooterInfo'] = self.footer_info.to_map()

        if self.hit_words is not None:
            result['HitWords'] = self.hit_words

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.refer_info is not None:
            result['ReferInfo'] = self.refer_info.to_map()

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.status is not None:
            result['Status'] = self.status

        if self.ticket_id is not None:
            result['TicketId'] = self.ticket_id

        if self.ticket_status is not None:
            result['TicketStatus'] = self.ticket_status

        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp

        if self.tip is not None:
            result['Tip'] = self.tip

        if self.type is not None:
            result['Type'] = self.type

        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.DialogBaseBodyAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('ChannelCode') is not None:
            self.channel_code = m.get('ChannelCode')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DataInfo') is not None:
            temp_model = main_models.DialogBaseBodyDataInfo()
            self.data_info = temp_model.from_map(m.get('DataInfo'))

        if m.get('DialogId') is not None:
            self.dialog_id = m.get('DialogId')

        if m.get('FooterInfo') is not None:
            temp_model = main_models.DialogBaseBodyFooterInfo()
            self.footer_info = temp_model.from_map(m.get('FooterInfo'))

        if m.get('HitWords') is not None:
            self.hit_words = m.get('HitWords')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('ReferInfo') is not None:
            temp_model = main_models.DialogBaseBody()
            self.refer_info = temp_model.from_map(m.get('ReferInfo'))

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TicketId') is not None:
            self.ticket_id = m.get('TicketId')

        if m.get('TicketStatus') is not None:
            self.ticket_status = m.get('TicketStatus')

        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')

        if m.get('Tip') is not None:
            self.tip = m.get('Tip')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UserInfo') is not None:
            temp_model = main_models.DialogBaseBodyUserInfo()
            self.user_info = temp_model.from_map(m.get('UserInfo'))

        return self

class DialogBaseBodyUserInfo(DaraModel):
    def __init__(
        self,
        avatar: str = None,
        role: int = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.avatar = avatar
        self.role = role
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avatar is not None:
            result['Avatar'] = self.avatar

        if self.role is not None:
            result['Role'] = self.role

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DialogBaseBodyFooterInfo(DaraModel):
    def __init__(
        self,
        ext: Dict[str, Any] = None,
        schema: str = None,
    ):
        self.ext = ext
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ext is not None:
            result['Ext'] = self.ext

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ext') is not None:
            self.ext = m.get('Ext')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self

class DialogBaseBodyDataInfo(DaraModel):
    def __init__(
        self,
        biz_id: str = None,
        biz_type: int = None,
        component: List[Dict[str, Any]] = None,
        container: Any = None,
        content: str = None,
        content_desensitized: str = None,
        editable: int = None,
        props: List[Dict[str, Any]] = None,
        schema: str = None,
        schema_id: int = None,
        service_channel: str = None,
        title: str = None,
        values: Dict[str, Any] = None,
    ):
        self.biz_id = biz_id
        self.biz_type = biz_type
        self.component = component
        self.container = container
        self.content = content
        self.content_desensitized = content_desensitized
        self.editable = editable
        self.props = props
        self.schema = schema
        self.schema_id = schema_id
        self.service_channel = service_channel
        self.title = title
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_id is not None:
            result['BizId'] = self.biz_id

        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.component is not None:
            result['Component'] = self.component

        if self.container is not None:
            result['Container'] = self.container

        if self.content is not None:
            result['Content'] = self.content

        if self.content_desensitized is not None:
            result['ContentDesensitized'] = self.content_desensitized

        if self.editable is not None:
            result['Editable'] = self.editable

        if self.props is not None:
            result['Props'] = self.props

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.schema_id is not None:
            result['SchemaId'] = self.schema_id

        if self.service_channel is not None:
            result['ServiceChannel'] = self.service_channel

        if self.title is not None:
            result['Title'] = self.title

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizId') is not None:
            self.biz_id = m.get('BizId')

        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('Component') is not None:
            self.component = m.get('Component')

        if m.get('Container') is not None:
            self.container = m.get('Container')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('ContentDesensitized') is not None:
            self.content_desensitized = m.get('ContentDesensitized')

        if m.get('Editable') is not None:
            self.editable = m.get('Editable')

        if m.get('Props') is not None:
            self.props = m.get('Props')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('SchemaId') is not None:
            self.schema_id = m.get('SchemaId')

        if m.get('ServiceChannel') is not None:
            self.service_channel = m.get('ServiceChannel')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self



class DialogBaseBodyAttachments(DaraModel):
    def __init__(
        self,
        name: str = None,
        size: str = None,
        type: str = None,
        url: str = None,
    ):
        self.name = name
        self.size = size
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

