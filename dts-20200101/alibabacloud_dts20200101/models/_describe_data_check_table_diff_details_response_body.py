# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dts20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDataCheckTableDiffDetailsResponseBody(DaraModel):
    def __init__(
        self,
        db_name: str = None,
        diff_count: int = None,
        diff_details: List[main_models.DescribeDataCheckTableDiffDetailsResponseBodyDiffDetails] = None,
        dynamic_message: str = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        instance_id: str = None,
        request_id: str = None,
        success: bool = None,
        tb_name: str = None,
    ):
        # The name of the source database to which the table that contains inconsistent data belongs.
        self.db_name = db_name
        # The number of data rows that contain inconsistent data.
        self.diff_count = diff_count
        # The information about the inconsistent data.
        self.diff_details = diff_details
        # The dynamic part in the error message. This parameter is used to replace the \\*\\*%s\\*\\* variable in the **ErrMessage** parameter.
        # 
        # > For example, if the value of the **ErrMessage** parameter is **The Value of Input Parameter %s is not valid** and the value of the **DynamicMessage** parameter is **Type**, the specified **Type** parameter is invalid.
        self.dynamic_message = dynamic_message
        # The error code returned if the request failed.
        self.err_code = err_code
        # The error message returned if the request failed.
        self.err_message = err_message
        # The HTTP status code returned.
        self.http_status_code = http_status_code
        # The instance ID.
        self.instance_id = instance_id
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success
        # The name of the table that contains inconsistent data in the source database.
        self.tb_name = tb_name

    def validate(self):
        if self.diff_details:
            for v1 in self.diff_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.diff_count is not None:
            result['DiffCount'] = self.diff_count

        result['DiffDetails'] = []
        if self.diff_details is not None:
            for k1 in self.diff_details:
                result['DiffDetails'].append(k1.to_map() if k1 else None)

        if self.dynamic_message is not None:
            result['DynamicMessage'] = self.dynamic_message

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.tb_name is not None:
            result['TbName'] = self.tb_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DiffCount') is not None:
            self.diff_count = m.get('DiffCount')

        self.diff_details = []
        if m.get('DiffDetails') is not None:
            for k1 in m.get('DiffDetails'):
                temp_model = main_models.DescribeDataCheckTableDiffDetailsResponseBodyDiffDetails()
                self.diff_details.append(temp_model.from_map(k1))

        if m.get('DynamicMessage') is not None:
            self.dynamic_message = m.get('DynamicMessage')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TbName') is not None:
            self.tb_name = m.get('TbName')

        return self

class DescribeDataCheckTableDiffDetailsResponseBodyDiffDetails(DaraModel):
    def __init__(
        self,
        diff: str = None,
        gmt_created: str = None,
        id: int = None,
    ):
        # The details of the inconsistent data, whose value is a JSON string. The JSON string contains the following parameters:
        # 
        # *   column: the name of the field.
        # *   source: the value of the field in the source database.
        # *   dest: the value of the field in the destination database.
        # *   isPrimary: indicates whether the field is a primary key.
        self.diff = diff
        # The time when the data verification was performed.
        self.gmt_created = gmt_created
        # The auto-increment primary key that is used to identify the data in a verification result.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.diff is not None:
            result['Diff'] = self.diff

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Diff') is not None:
            self.diff = m.get('Diff')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

