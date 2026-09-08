# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadMessageListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ReadMessageListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned when the call fails. For more information, see error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The error message returned when the call fails.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values: true: The call was successful. false: The call failed.
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
            temp_model = main_models.ReadMessageListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadMessageListResponseBodyData(DaraModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        page_size: int = None,
        rows: List[main_models.ReadMessageListResponseBodyDataRows] = None,
    ):
        # The number of messages.
        self.count = count
        # A reserved field.
        self.max_results = max_results
        # A reserved field.
        self.next_token = next_token
        # The page number.
        self.page = page
        # The page size.
        self.page_size = page_size
        # The returned data.
        self.rows = rows

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page is not None:
            result['Page'] = self.page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['Rows'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Page') is not None:
            self.page = m.get('Page')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.rows = []
        if m.get('Rows') is not None:
            for k1 in m.get('Rows'):
                temp_model = main_models.ReadMessageListResponseBodyDataRows()
                self.rows.append(temp_model.from_map(k1))

        return self

class ReadMessageListResponseBodyDataRows(DaraModel):
    def __init__(
        self,
        category_code: str = None,
        category_name: str = None,
        class_: str = None,
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
        titleh: str = None,
    ):
        # The category code.
        self.category_code = category_code
        # The message category name.
        self.category_name = category_name
        # A reserved field.
        self.class_ = class_
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
        # The read status. A value of 0 indicates unread. A value of 1 indicates read.
        self.status = status
        # The message title.
        self.title = title
        # The highlighted title.
        self.titleh = titleh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.class_ is not None:
            result['Class'] = self.class_

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

        if self.titleh is not None:
            result['Titleh'] = self.titleh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Class') is not None:
            self.class_ = m.get('Class')

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

        if m.get('Titleh') is not None:
            self.titleh = m.get('Titleh')

        return self

