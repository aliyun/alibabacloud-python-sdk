# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class CompareCopyRuleVariableResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: main_models.CompareCopyRuleVariableResponseBodyResultObject = None,
    ):
        # Id of the request
        self.request_id = request_id
        # Result object.
        self.result_object = result_object

    def validate(self):
        if self.result_object:
            self.result_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObject()
            self.result_object = temp_model.from_map(m.get('ResultObject'))

        return self

class CompareCopyRuleVariableResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        cust_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectCustVariableList] = None,
        event_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectEventVariableList] = None,
        expression_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectExpressionVariableList] = None,
        name_list_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectNameListVariableList] = None,
        query_expression_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectQueryExpressionVariableList] = None,
        system_variable_list: List[main_models.CompareCopyRuleVariableResponseBodyResultObjectSystemVariableList] = None,
    ):
        # Cumulative variable list
        self.cust_variable_list = cust_variable_list
        # Event field variables
        self.event_variable_list = event_variable_list
        # Custom variable list
        self.expression_variable_list = expression_variable_list
        # Name list variables
        self.name_list_variable_list = name_list_variable_list
        # Custom Query Variable List
        self.query_expression_variable_list = query_expression_variable_list
        # System variable list
        self.system_variable_list = system_variable_list

    def validate(self):
        if self.cust_variable_list:
            for v1 in self.cust_variable_list:
                 if v1:
                    v1.validate()
        if self.event_variable_list:
            for v1 in self.event_variable_list:
                 if v1:
                    v1.validate()
        if self.expression_variable_list:
            for v1 in self.expression_variable_list:
                 if v1:
                    v1.validate()
        if self.name_list_variable_list:
            for v1 in self.name_list_variable_list:
                 if v1:
                    v1.validate()
        if self.query_expression_variable_list:
            for v1 in self.query_expression_variable_list:
                 if v1:
                    v1.validate()
        if self.system_variable_list:
            for v1 in self.system_variable_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustVariableList'] = []
        if self.cust_variable_list is not None:
            for k1 in self.cust_variable_list:
                result['CustVariableList'].append(k1.to_map() if k1 else None)

        result['EventVariableList'] = []
        if self.event_variable_list is not None:
            for k1 in self.event_variable_list:
                result['EventVariableList'].append(k1.to_map() if k1 else None)

        result['ExpressionVariableList'] = []
        if self.expression_variable_list is not None:
            for k1 in self.expression_variable_list:
                result['ExpressionVariableList'].append(k1.to_map() if k1 else None)

        result['NameListVariableList'] = []
        if self.name_list_variable_list is not None:
            for k1 in self.name_list_variable_list:
                result['NameListVariableList'].append(k1.to_map() if k1 else None)

        result['QueryExpressionVariableList'] = []
        if self.query_expression_variable_list is not None:
            for k1 in self.query_expression_variable_list:
                result['QueryExpressionVariableList'].append(k1.to_map() if k1 else None)

        result['SystemVariableList'] = []
        if self.system_variable_list is not None:
            for k1 in self.system_variable_list:
                result['SystemVariableList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cust_variable_list = []
        if m.get('CustVariableList') is not None:
            for k1 in m.get('CustVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectCustVariableList()
                self.cust_variable_list.append(temp_model.from_map(k1))

        self.event_variable_list = []
        if m.get('EventVariableList') is not None:
            for k1 in m.get('EventVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectEventVariableList()
                self.event_variable_list.append(temp_model.from_map(k1))

        self.expression_variable_list = []
        if m.get('ExpressionVariableList') is not None:
            for k1 in m.get('ExpressionVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectExpressionVariableList()
                self.expression_variable_list.append(temp_model.from_map(k1))

        self.name_list_variable_list = []
        if m.get('NameListVariableList') is not None:
            for k1 in m.get('NameListVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectNameListVariableList()
                self.name_list_variable_list.append(temp_model.from_map(k1))

        self.query_expression_variable_list = []
        if m.get('QueryExpressionVariableList') is not None:
            for k1 in m.get('QueryExpressionVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectQueryExpressionVariableList()
                self.query_expression_variable_list.append(temp_model.from_map(k1))

        self.system_variable_list = []
        if m.get('SystemVariableList') is not None:
            for k1 in m.get('SystemVariableList'):
                temp_model = main_models.CompareCopyRuleVariableResponseBodyResultObjectSystemVariableList()
                self.system_variable_list.append(temp_model.from_map(k1))

        return self

class CompareCopyRuleVariableResponseBodyResultObjectSystemVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable ID
        self.id = id
        # Variable name
        self.name = name
        # Variable type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CompareCopyRuleVariableResponseBodyResultObjectQueryExpressionVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable ID
        self.id = id
        # Variable Name
        self.name = name
        # Variable Type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CompareCopyRuleVariableResponseBodyResultObjectNameListVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable id
        self.id = id
        # Variable name
        self.name = name
        # Variable type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CompareCopyRuleVariableResponseBodyResultObjectExpressionVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable ID
        self.id = id
        # Variable name
        self.name = name
        # Variable Type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CompareCopyRuleVariableResponseBodyResultObjectEventVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable id
        self.id = id
        # Variable name
        self.name = name
        # Variable type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class CompareCopyRuleVariableResponseBodyResultObjectCustVariableList(DaraModel):
    def __init__(
        self,
        description: str = None,
        id: int = None,
        name: str = None,
        out_type: str = None,
        title: str = None,
    ):
        # Description
        self.description = description
        # Variable ID
        self.id = id
        # Variable name
        self.name = name
        # Variable type
        self.out_type = out_type
        # Title
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.out_type is not None:
            result['OutType'] = self.out_type

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutType') is not None:
            self.out_type = m.get('OutType')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

