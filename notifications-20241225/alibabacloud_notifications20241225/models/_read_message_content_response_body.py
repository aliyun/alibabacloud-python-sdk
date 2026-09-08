# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadMessageContentResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ReadMessageContentResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned when the call fails. For more information, refer to error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The error message returned when the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReadMessageContentResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadMessageContentResponseBodyData(DaraModel):
    def __init__(
        self,
        datas: main_models.ReadMessageContentResponseBodyDataDatas = None,
    ):
        # The list of degradation rules.
        self.datas = datas

    def validate(self):
        if self.datas:
            self.datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datas is not None:
            result['Datas'] = self.datas.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Datas') is not None:
            temp_model = main_models.ReadMessageContentResponseBodyDataDatas()
            self.datas = temp_model.from_map(m.get('Datas'))

        return self

class ReadMessageContentResponseBodyDataDatas(DaraModel):
    def __init__(
        self,
        item: List[main_models.ReadMessageContentResponseBodyDataDatasItem] = None,
        last_item: List[main_models.ReadMessageContentResponseBodyDataDatasLastItem] = None,
        next_item: List[main_models.ReadMessageContentResponseBodyDataDatasNextItem] = None,
    ):
        # The data item.
        self.item = item
        # /
        self.last_item = last_item
        # /
        self.next_item = next_item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()
        if self.last_item:
            for v1 in self.last_item:
                 if v1:
                    v1.validate()
        if self.next_item:
            for v1 in self.next_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        result['LastItem'] = []
        if self.last_item is not None:
            for k1 in self.last_item:
                result['LastItem'].append(k1.to_map() if k1 else None)

        result['NextItem'] = []
        if self.next_item is not None:
            for k1 in self.next_item:
                result['NextItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.ReadMessageContentResponseBodyDataDatasItem()
                self.item.append(temp_model.from_map(k1))

        self.last_item = []
        if m.get('LastItem') is not None:
            for k1 in m.get('LastItem'):
                temp_model = main_models.ReadMessageContentResponseBodyDataDatasLastItem()
                self.last_item.append(temp_model.from_map(k1))

        self.next_item = []
        if m.get('NextItem') is not None:
            for k1 in m.get('NextItem'):
                temp_model = main_models.ReadMessageContentResponseBodyDataDatasNextItem()
                self.next_item.append(temp_model.from_map(k1))

        return self

class ReadMessageContentResponseBodyDataDatasNextItem(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        # The message category name.
        self.category_name = category_name
        # The message class ID.
        self.class_id = class_id
        # The message content.
        self.content = content
        # The deletion flag.
        self.deleted = deleted
        # The time when the message was created.
        self.gmt_created = gmt_created
        # The time when the message was updated.
        self.gmt_update = gmt_update
        # A reserved field.
        self.mass_id = mass_id
        # A reserved field.
        self.memo = memo
        # The message ID.
        self.msg_id = msg_id
        # The read status. Valid values:
        # - 0: unread
        # - 1: read.
        self.status = status
        # The message title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.content is not None:
            result['Content'] = self.content

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update

        if self.mass_id is not None:
            result['MassId'] = self.mass_id

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')

        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ReadMessageContentResponseBodyDataDatasLastItem(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        # The message category name.
        self.category_name = category_name
        # The message class ID.
        self.class_id = class_id
        # The message content.
        self.content = content
        # The deletion flag.
        self.deleted = deleted
        # The time when the message was created.
        self.gmt_created = gmt_created
        # The time when the message was updated.
        self.gmt_update = gmt_update
        # A reserved field.
        self.mass_id = mass_id
        # A reserved field.
        self.memo = memo
        # The message ID.
        self.msg_id = msg_id
        # The read status. Valid values:
        # - 0: unread
        # - 1: read.
        self.status = status
        # The message title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.content is not None:
            result['Content'] = self.content

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update

        if self.mass_id is not None:
            result['MassId'] = self.mass_id

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')

        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class ReadMessageContentResponseBodyDataDatasItem(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        class_id: int = None,
        content: str = None,
        deleted: int = None,
        gmt_created: int = None,
        gmt_update: int = None,
        mass_id: int = None,
        memo: str = None,
        msg_id: int = None,
        status: int = None,
        title: str = None,
    ):
        # The message category name.
        self.category_name = category_name
        # The message class ID.
        self.class_id = class_id
        # The message content.
        self.content = content
        # The deletion flag.
        self.deleted = deleted
        # The time when the message was created.
        self.gmt_created = gmt_created
        # The time when the message was updated.
        self.gmt_update = gmt_update
        # A reserved field.
        self.mass_id = mass_id
        # A reserved field.
        self.memo = memo
        # The message ID.
        self.msg_id = msg_id
        # The read status. Valid values:
        # - 0: unread
        # - 1: read.
        self.status = status
        # The message title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.class_id is not None:
            result['ClassId'] = self.class_id

        if self.content is not None:
            result['Content'] = self.content

        if self.deleted is not None:
            result['Deleted'] = self.deleted

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_update is not None:
            result['GmtUpdate'] = self.gmt_update

        if self.mass_id is not None:
            result['MassId'] = self.mass_id

        if self.memo is not None:
            result['Memo'] = self.memo

        if self.msg_id is not None:
            result['MsgId'] = self.msg_id

        if self.status is not None:
            result['Status'] = self.status

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('ClassId') is not None:
            self.class_id = m.get('ClassId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtUpdate') is not None:
            self.gmt_update = m.get('GmtUpdate')

        if m.get('MassId') is not None:
            self.mass_id = m.get('MassId')

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

