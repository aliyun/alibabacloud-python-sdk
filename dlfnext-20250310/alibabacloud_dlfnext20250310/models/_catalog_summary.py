# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from alibabacloud_dlfnext20250310 import models as main_models 


class CatalogSummary(DaraModel):
    def __init__(
        self,
        api_visit_count_monthly: int = None,
        database_count: main_models.MoMValues = None,
        file_access_count_monthly: int = None,
        generated_date: str = None,
        obj_type_archive_size: int = None,
        obj_type_cold_archive_size: int = None,
        obj_type_ia_size: int = None,
        obj_type_standard_size: int = None,
        partition_count: main_models.MoMValues = None,
        table_count: main_models.MoMValues = None,
        throughput_monthly: int = None,
        total_file_count: main_models.MoMValues = None,
        total_file_size_in_bytes: main_models.MoMValues = None,
    ):
        self.api_visit_count_monthly = api_visit_count_monthly
        self.database_count = database_count
        self.file_access_count_monthly = file_access_count_monthly
        # Update date of the statistics
        self.generated_date = generated_date
        self.obj_type_archive_size = obj_type_archive_size
        self.obj_type_cold_archive_size = obj_type_cold_archive_size
        self.obj_type_ia_size = obj_type_ia_size
        self.obj_type_standard_size = obj_type_standard_size
        self.partition_count = partition_count
        self.table_count = table_count
        self.throughput_monthly = throughput_monthly
        self.total_file_count = total_file_count
        self.total_file_size_in_bytes = total_file_size_in_bytes

    def validate(self):
        if self.database_count:
            self.database_count.validate()
        if self.partition_count:
            self.partition_count.validate()
        if self.table_count:
            self.table_count.validate()
        if self.total_file_count:
            self.total_file_count.validate()
        if self.total_file_size_in_bytes:
            self.total_file_size_in_bytes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_visit_count_monthly is not None:
            result['apiVisitCountMonthly'] = self.api_visit_count_monthly

        if self.database_count is not None:
            result['databaseCount'] = self.database_count.to_map()

        if self.file_access_count_monthly is not None:
            result['fileAccessCountMonthly'] = self.file_access_count_monthly

        if self.generated_date is not None:
            result['generatedDate'] = self.generated_date

        if self.obj_type_archive_size is not None:
            result['objTypeArchiveSize'] = self.obj_type_archive_size

        if self.obj_type_cold_archive_size is not None:
            result['objTypeColdArchiveSize'] = self.obj_type_cold_archive_size

        if self.obj_type_ia_size is not None:
            result['objTypeIaSize'] = self.obj_type_ia_size

        if self.obj_type_standard_size is not None:
            result['objTypeStandardSize'] = self.obj_type_standard_size

        if self.partition_count is not None:
            result['partitionCount'] = self.partition_count.to_map()

        if self.table_count is not None:
            result['tableCount'] = self.table_count.to_map()

        if self.throughput_monthly is not None:
            result['throughputMonthly'] = self.throughput_monthly

        if self.total_file_count is not None:
            result['totalFileCount'] = self.total_file_count.to_map()

        if self.total_file_size_in_bytes is not None:
            result['totalFileSizeInBytes'] = self.total_file_size_in_bytes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiVisitCountMonthly') is not None:
            self.api_visit_count_monthly = m.get('apiVisitCountMonthly')

        if m.get('databaseCount') is not None:
            temp_model = main_models.MoMValues()
            self.database_count = temp_model.from_map(m.get('databaseCount'))

        if m.get('fileAccessCountMonthly') is not None:
            self.file_access_count_monthly = m.get('fileAccessCountMonthly')

        if m.get('generatedDate') is not None:
            self.generated_date = m.get('generatedDate')

        if m.get('objTypeArchiveSize') is not None:
            self.obj_type_archive_size = m.get('objTypeArchiveSize')

        if m.get('objTypeColdArchiveSize') is not None:
            self.obj_type_cold_archive_size = m.get('objTypeColdArchiveSize')

        if m.get('objTypeIaSize') is not None:
            self.obj_type_ia_size = m.get('objTypeIaSize')

        if m.get('objTypeStandardSize') is not None:
            self.obj_type_standard_size = m.get('objTypeStandardSize')

        if m.get('partitionCount') is not None:
            temp_model = main_models.MoMValues()
            self.partition_count = temp_model.from_map(m.get('partitionCount'))

        if m.get('tableCount') is not None:
            temp_model = main_models.MoMValues()
            self.table_count = temp_model.from_map(m.get('tableCount'))

        if m.get('throughputMonthly') is not None:
            self.throughput_monthly = m.get('throughputMonthly')

        if m.get('totalFileCount') is not None:
            temp_model = main_models.MoMValues()
            self.total_file_count = temp_model.from_map(m.get('totalFileCount'))

        if m.get('totalFileSizeInBytes') is not None:
            temp_model = main_models.MoMValues()
            self.total_file_size_in_bytes = temp_model.from_map(m.get('totalFileSizeInBytes'))

        return self

