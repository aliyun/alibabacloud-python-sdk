# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class GetMetaCompareIncrementDbOverviewResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetMetaCompareIncrementDbOverviewResponseBodyData = None,
        err_code: str = None,
        err_message: str = None,
        success: bool = None,
    ):
        # The list of data returned by the API operation. For the element structure, see the descriptions of the child fields.
        self.data = data
        # The fault message code.
        self.err_code = err_code
        # The error message.
        self.err_message = err_message
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed. If the call fails, troubleshoot the issue based on errCode and errMessage.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetMetaCompareIncrementDbOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMetaCompareIncrementDbOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        compare_job_id: int = None,
        cur_version_time: str = None,
        diff_add_partition_num: int = None,
        diff_add_table_num: int = None,
        diff_del_partition_num: int = None,
        diff_del_table_num: int = None,
        diff_modify_partition_num: int = None,
        diff_modify_table_num: int = None,
        diff_partition_num: int = None,
        diff_table_num: int = None,
        prev_version_time: str = None,
    ):
        # The unique identifier of the current metadata comparison job.
        self.compare_job_id = compare_job_id
        # The metadata version time corresponding to the current comparison.
        self.cur_version_time = cur_version_time
        # The number of partitions added compared to the last comparison.
        self.diff_add_partition_num = diff_add_partition_num
        # The number of tables added compared to the last comparison.
        self.diff_add_table_num = diff_add_table_num
        # The number of partitions deleted compared to the last comparison.
        self.diff_del_partition_num = diff_del_partition_num
        # The number of tables deleted compared to the last comparison.
        self.diff_del_table_num = diff_del_table_num
        # The number of partitions whose properties changed compared to the last comparison.
        self.diff_modify_partition_num = diff_modify_partition_num
        # The number of tables whose structure underwent schema evolution compared to the last comparison.
        self.diff_modify_table_num = diff_modify_table_num
        # The total number of differences at the partition level, which is the sum of the number of added, deleted, and modified partitions.
        self.diff_partition_num = diff_partition_num
        # The total number of differences at the table level, which is the sum of the number of added, deleted, and modified tables.
        self.diff_table_num = diff_table_num
        # The metadata version time corresponding to the last comparison.
        self.prev_version_time = prev_version_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compare_job_id is not None:
            result['compareJobId'] = self.compare_job_id

        if self.cur_version_time is not None:
            result['curVersionTime'] = self.cur_version_time

        if self.diff_add_partition_num is not None:
            result['diffAddPartitionNum'] = self.diff_add_partition_num

        if self.diff_add_table_num is not None:
            result['diffAddTableNum'] = self.diff_add_table_num

        if self.diff_del_partition_num is not None:
            result['diffDelPartitionNum'] = self.diff_del_partition_num

        if self.diff_del_table_num is not None:
            result['diffDelTableNum'] = self.diff_del_table_num

        if self.diff_modify_partition_num is not None:
            result['diffModifyPartitionNum'] = self.diff_modify_partition_num

        if self.diff_modify_table_num is not None:
            result['diffModifyTableNum'] = self.diff_modify_table_num

        if self.diff_partition_num is not None:
            result['diffPartitionNum'] = self.diff_partition_num

        if self.diff_table_num is not None:
            result['diffTableNum'] = self.diff_table_num

        if self.prev_version_time is not None:
            result['prevVersionTime'] = self.prev_version_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('compareJobId') is not None:
            self.compare_job_id = m.get('compareJobId')

        if m.get('curVersionTime') is not None:
            self.cur_version_time = m.get('curVersionTime')

        if m.get('diffAddPartitionNum') is not None:
            self.diff_add_partition_num = m.get('diffAddPartitionNum')

        if m.get('diffAddTableNum') is not None:
            self.diff_add_table_num = m.get('diffAddTableNum')

        if m.get('diffDelPartitionNum') is not None:
            self.diff_del_partition_num = m.get('diffDelPartitionNum')

        if m.get('diffDelTableNum') is not None:
            self.diff_del_table_num = m.get('diffDelTableNum')

        if m.get('diffModifyPartitionNum') is not None:
            self.diff_modify_partition_num = m.get('diffModifyPartitionNum')

        if m.get('diffModifyTableNum') is not None:
            self.diff_modify_table_num = m.get('diffModifyTableNum')

        if m.get('diffPartitionNum') is not None:
            self.diff_partition_num = m.get('diffPartitionNum')

        if m.get('diffTableNum') is not None:
            self.diff_table_num = m.get('diffTableNum')

        if m.get('prevVersionTime') is not None:
            self.prev_version_time = m.get('prevVersionTime')

        return self

