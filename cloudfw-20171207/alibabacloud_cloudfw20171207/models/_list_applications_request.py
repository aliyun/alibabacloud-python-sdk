# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListApplicationsRequest(DaraModel):
    def __init__(
        self,
        application_id: int = None,
        application_name: str = None,
        category_id: int = None,
        category_name: str = None,
        description: str = None,
        group_name: str = None,
        lang: str = None,
        page_no: int = None,
        page_size: int = None,
        risk: str = None,
        technology: str = None,
    ):
        # The application ID. Exact match is supported.
        self.application_id = application_id
        # The application name. Fuzzy match is supported.
        self.application_name = application_name
        # The application category ID. Exact match is supported.
        self.category_id = category_id
        # The application category name. Fuzzy match is supported.
        self.category_name = category_name
        # The application description. Fuzzy match is supported.
        self.description = description
        # The application group name. Fuzzy match is supported.
        self.group_name = group_name
        # The language of the returned information. Valid values:
        # - **zh**: Chinese. This is the default value.
        # - **en**: English.
        # This parameter determines whether the application name, category name, technology type, vendor, and description are returned in Chinese or English.
        self.lang = lang
        # The page number. Pages start from 1. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. The value must be greater than or equal to 1. Default value: 10.
        self.page_size = page_size
        # The risk level. Exact match is supported. Valid values:
        # - **Information**: Informational.
        # - **Low**: Low.
        # - **Medium**: Medium.
        # - **High**: High.
        # - **Critical**: Critical.
        # If an invalid value is passed, this filter condition is ignored.
        self.risk = risk
        # The technology type name. Fuzzy match is supported.
        self.technology = technology

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.description is not None:
            result['Description'] = self.description

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.risk is not None:
            result['Risk'] = self.risk

        if self.technology is not None:
            result['Technology'] = self.technology

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Risk') is not None:
            self.risk = m.get('Risk')

        if m.get('Technology') is not None:
            self.technology = m.get('Technology')

        return self

