# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListSQLReviewOriginSQLRequest(DaraModel):
    def __init__(
        self,
        order_action_detail: main_models.ListSQLReviewOriginSQLRequestOrderActionDetail = None,
        order_id: int = None,
        tid: int = None,
    ):
        # The parameters that are used to filter SQL statements involved in the ticket.
        self.order_action_detail = order_action_detail
        # The ID of the SQL review ticket. You can call the [CreateSQLReviewOrder](https://help.aliyun.com/document_detail/257777.html) operation to query the ticket ID.
        # 
        # This parameter is required.
        self.order_id = order_id
        # The tenant ID. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid

    def validate(self):
        if self.order_action_detail:
            self.order_action_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.order_action_detail is not None:
            result['OrderActionDetail'] = self.order_action_detail.to_map()

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrderActionDetail') is not None:
            temp_model = main_models.ListSQLReviewOriginSQLRequestOrderActionDetail()
            self.order_action_detail = temp_model.from_map(m.get('OrderActionDetail'))

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class ListSQLReviewOriginSQLRequestOrderActionDetail(DaraModel):
    def __init__(
        self,
        check_status_result: str = None,
        file_id: int = None,
        page: main_models.ListSQLReviewOriginSQLRequestOrderActionDetailPage = None,
        sqlreview_result: str = None,
    ):
        # The review status of the SQL statement. Valid values:
        # 
        # *   **new**: The SQL statement was waiting to be reviewed.
        # *   **unknown**: The SQL statement cannot be parsed.
        # *   **check_not_pass**: The SQL statement failed to pass the review.
        # *   **check_pass**: The SQL statement passed the review.
        # *   **force_pass**: The SQL statement passed the manual review.
        # *   **force_not_pass**: The SQL statement failed to pass the manual review.
        self.check_status_result = check_status_result
        # The ID of the file that contains the SQL statements to be reviewed.
        self.file_id = file_id
        # The pagination information.
        self.page = page
        # The optimization suggestion for the SQL statement. Valid values:
        # 
        # *   **MUST_IMPROVE**: The SQL statement must be optimized.
        # *   **POTENTIAL_ISSUE**: The SQL statement contains potential issues.
        # *   **SUGGEST_IMPROVE**: We recommend that you optimize the SQL statement.
        # *   **USE_DMS_TOOLKIT**: We recommend that you change schemas without locking tables.
        # *   **USE_DMS_DML_UNLOCK**: We recommend that you change data without locking tables.
        # *   **TABLE_INDEX_SUGGEST**: We recommend that you optimize indexes for the SQL statement.
        self.sqlreview_result = sqlreview_result

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_status_result is not None:
            result['CheckStatusResult'] = self.check_status_result

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.page is not None:
            result['Page'] = self.page.to_map()

        if self.sqlreview_result is not None:
            result['SQLReviewResult'] = self.sqlreview_result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckStatusResult') is not None:
            self.check_status_result = m.get('CheckStatusResult')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Page') is not None:
            temp_model = main_models.ListSQLReviewOriginSQLRequestOrderActionDetailPage()
            self.page = temp_model.from_map(m.get('Page'))

        if m.get('SQLReviewResult') is not None:
            self.sqlreview_result = m.get('SQLReviewResult')

        return self

class ListSQLReviewOriginSQLRequestOrderActionDetailPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

