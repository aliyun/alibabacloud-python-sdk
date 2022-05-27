# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class AssociatePrincipalWithPortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # RAM实体ID
        self.principal_id = principal_id
        # RAM实体类型
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class AssociatePrincipalWithPortfolioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociatePrincipalWithPortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociatePrincipalWithPortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociatePrincipalWithPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateProductWithPortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        product_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class AssociateProductWithPortfolioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateProductWithPortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateProductWithPortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateProductWithPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConstraintRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        constraint_type: str = None,
        description: str = None,
        portfolio_id: str = None,
        product_id: str = None,
    ):
        # 约束配置
        self.config = config
        # 约束类型
        self.constraint_type = constraint_type
        # 约束描述
        self.description = description
        # 约束所属的产品组合ID
        self.portfolio_id = portfolio_id
        # 约束对应的产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class CreateConstraintResponseBody(TeaModel):
    def __init__(
        self,
        constraint_id: str = None,
        request_id: str = None,
    ):
        # 约束ID
        self.constraint_id = constraint_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateConstraintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateConstraintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePortfolioRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 产品组合描述
        self.description = description
        # 产品组合名称
        self.portfolio_name = portfolio_name
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreatePortfolioResponseBody(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        request_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreatePortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreatePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductRequestProductVersionParameters(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # 是否启用
        self.active = active
        # 产品版本描述
        self.description = description
        # 推荐信息
        self.guidance = guidance
        # 产品版本名称
        self.product_version_name = product_version_name
        # 模板类型
        self.template_type = template_type
        # 模板的URL地址
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        product_name: str = None,
        product_type: str = None,
        product_version_parameters: CreateProductRequestProductVersionParameters = None,
        provider_name: str = None,
    ):
        # 产品描述
        self.description = description
        # 产品名称
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 产品版本相关的参数
        self.product_version_parameters = product_version_parameters
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        if self.product_version_parameters:
            self.product_version_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_version_parameters is not None:
            result['ProductVersionParameters'] = self.product_version_parameters.to_map()
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductVersionParameters') is not None:
            temp_model = CreateProductRequestProductVersionParameters()
            self.product_version_parameters = temp_model.from_map(m['ProductVersionParameters'])
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreateProductShrinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        product_name: str = None,
        product_type: str = None,
        product_version_parameters_shrink: str = None,
        provider_name: str = None,
    ):
        # 产品描述
        self.description = description
        # 产品名称
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 产品版本相关的参数
        self.product_version_parameters_shrink = product_version_parameters_shrink
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.product_version_parameters_shrink is not None:
            result['ProductVersionParameters'] = self.product_version_parameters_shrink
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProductVersionParameters') is not None:
            self.product_version_parameters_shrink = m.get('ProductVersionParameters')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class CreateProductResponseBody(TeaModel):
    def __init__(
        self,
        product_id: str = None,
        product_version_id: str = None,
        request_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id
        self.product_version_id = product_version_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProductVersionRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # 是否启用
        self.active = active
        # 产品版本描述
        self.description = description
        # 推荐信息
        self.guidance = guidance
        # 产品版本所属的产品ID
        self.product_id = product_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 模板类型
        self.template_type = template_type
        # 模板的OSS地址
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        product_version_id: str = None,
        request_id: str = None,
    ):
        # 产品版本ID
        self.product_version_id = product_version_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_body: str = None,
        template_type: str = None,
    ):
        # 模板内容
        self.template_body = template_body
        # 模板类型
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_url: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 模板的OSS地址
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConstraintRequest(TeaModel):
    def __init__(
        self,
        constraint_id: str = None,
    ):
        # 约束ID
        self.constraint_id = constraint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        return self


class DeleteConstraintResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConstraintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteConstraintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeletePortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class DeletePortfolioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeletePortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DeleteProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProductVersionRequest(TeaModel):
    def __init__(
        self,
        product_version_id: str = None,
    ):
        # 产品版本ID
        self.product_version_id = product_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class DeleteProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociatePrincipalFromPortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # RAM实体ID
        self.principal_id = principal_id
        # RAM实体类型
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class DisassociatePrincipalFromPortfolioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociatePrincipalFromPortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociatePrincipalFromPortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociatePrincipalFromPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateProductFromPortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        product_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class DisassociateProductFromPortfolioResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateProductFromPortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DisassociateProductFromPortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateProductFromPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConstraintRequest(TeaModel):
    def __init__(
        self,
        constraint_id: str = None,
    ):
        # 约束ID
        self.constraint_id = constraint_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        return self


class GetConstraintResponseBodyConstraintDetail(TeaModel):
    def __init__(
        self,
        config: str = None,
        constraint_id: str = None,
        constraint_type: str = None,
        create_time: str = None,
        description: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
    ):
        # 约束配置
        self.config = config
        # 约束ID
        self.constraint_id = constraint_id
        # 约束类型
        self.constraint_type = constraint_type
        # 创建时间
        self.create_time = create_time
        # 描述
        self.description = description
        # 约束所属的产品组合ID
        self.portfolio_id = portfolio_id
        # 约束的产品ID
        self.product_id = product_id
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class GetConstraintResponseBody(TeaModel):
    def __init__(
        self,
        constraint_detail: GetConstraintResponseBodyConstraintDetail = None,
        request_id: str = None,
    ):
        # 约束详情
        self.constraint_detail = constraint_detail
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.constraint_detail:
            self.constraint_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_detail is not None:
            result['ConstraintDetail'] = self.constraint_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintDetail') is not None:
            temp_model = GetConstraintResponseBodyConstraintDetail()
            self.constraint_detail = temp_model.from_map(m['ConstraintDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetConstraintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetConstraintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPortfolioRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class GetPortfolioResponseBodyPortfolioDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        portfolio_arn: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 产品组合创建时间
        self.create_time = create_time
        # 产品组合描述
        self.description = description
        # 产品组合ARN
        self.portfolio_arn = portfolio_arn
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品组合名称
        self.portfolio_name = portfolio_name
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_arn is not None:
            result['PortfolioArn'] = self.portfolio_arn
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioArn') is not None:
            self.portfolio_arn = m.get('PortfolioArn')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetPortfolioResponseBody(TeaModel):
    def __init__(
        self,
        portfolio_detail: GetPortfolioResponseBodyPortfolioDetail = None,
        request_id: str = None,
    ):
        # 产品组合详情
        self.portfolio_detail = portfolio_detail
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.portfolio_detail:
            self.portfolio_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_detail is not None:
            result['PortfolioDetail'] = self.portfolio_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioDetail') is not None:
            temp_model = GetPortfolioResponseBodyPortfolioDetail()
            self.portfolio_detail = temp_model.from_map(m['PortfolioDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductAsAdminRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class GetProductAsAdminResponseBodyProductDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 产品描述
        self.description = description
        # 产品ARN
        self.product_arn = product_arn
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetProductAsAdminResponseBody(TeaModel):
    def __init__(
        self,
        product_detail: GetProductAsAdminResponseBodyProductDetail = None,
        request_id: str = None,
    ):
        # 产品详情
        self.product_detail = product_detail
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.product_detail:
            self.product_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_detail is not None:
            result['ProductDetail'] = self.product_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductDetail') is not None:
            temp_model = GetProductAsAdminResponseBodyProductDetail()
            self.product_detail = temp_model.from_map(m['ProductDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductAsAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductAsAdminResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductAsAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductAsEndUserRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class GetProductAsEndUserResponseBodyProductSummary(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        has_default_launch_option: bool = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 产品描述
        self.description = description
        self.has_default_launch_option = has_default_launch_option
        # 产品ARN
        self.product_arn = product_arn
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.has_default_launch_option is not None:
            result['HasDefaultLaunchOption'] = self.has_default_launch_option
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasDefaultLaunchOption') is not None:
            self.has_default_launch_option = m.get('HasDefaultLaunchOption')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class GetProductAsEndUserResponseBody(TeaModel):
    def __init__(
        self,
        product_summary: GetProductAsEndUserResponseBodyProductSummary = None,
        request_id: str = None,
    ):
        # 产品详情
        self.product_summary = product_summary
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.product_summary:
            self.product_summary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_summary is not None:
            result['ProductSummary'] = self.product_summary.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductSummary') is not None:
            temp_model = GetProductAsEndUserResponseBodyProductSummary()
            self.product_summary = temp_model.from_map(m['ProductSummary'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductAsEndUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductAsEndUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductAsEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProductVersionRequest(TeaModel):
    def __init__(
        self,
        product_version_id: str = None,
    ):
        # 产品版本ID
        self.product_version_id = product_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class GetProductVersionResponseBodyProductVersionDetail(TeaModel):
    def __init__(
        self,
        active: bool = None,
        create_time: str = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # 是否启用
        self.active = active
        # 创建时间
        self.create_time = create_time
        # 产品版本描述
        self.description = description
        # 推荐信息
        self.guidance = guidance
        # 产品版本所属的产品ID
        self.product_id = product_id
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 模板类型
        self.template_type = template_type
        # 模板的OSS地址
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class GetProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        product_version_detail: GetProductVersionResponseBodyProductVersionDetail = None,
        request_id: str = None,
    ):
        # 产品版本详情
        self.product_version_detail = product_version_detail
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.product_version_detail:
            self.product_version_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_detail is not None:
            result['ProductVersionDetail'] = self.product_version_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionDetail') is not None:
            temp_model = GetProductVersionResponseBodyProductVersionDetail()
            self.product_version_detail = temp_model.from_map(m['ProductVersionDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProvisionedProductRequest(TeaModel):
    def __init__(
        self,
        provisioned_product_id: str = None,
    ):
        # 实例ID
        self.provisioned_product_id = provisioned_product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        return self


class GetProvisionedProductResponseBodyProvisionedProductDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        last_provisioning_task_id: str = None,
        last_successful_provisioning_task_id: str = None,
        last_task_id: str = None,
        owner_principal_id: str = None,
        owner_principal_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_arn: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        provisioned_product_type: str = None,
        stack_id: str = None,
        stack_region_id: str = None,
        status: str = None,
        status_message: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 上一次执行的实例操作任务ID
        self.last_provisioning_task_id = last_provisioning_task_id
        # 上一次成功执行的实例操作任务ID
        self.last_successful_provisioning_task_id = last_successful_provisioning_task_id
        # 上一次执行的任务ID
        self.last_task_id = last_task_id
        # 归属人的RAM实体ID
        self.owner_principal_id = owner_principal_id
        # 归属人的RAM实体类型
        self.owner_principal_type = owner_principal_type
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 实例ARN
        self.provisioned_product_arn = provisioned_product_arn
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 实例名称
        self.provisioned_product_name = provisioned_product_name
        self.provisioned_product_type = provisioned_product_type
        # ROS资源栈的ID
        self.stack_id = stack_id
        # ROS资源栈所属的地域ID
        self.stack_region_id = stack_region_id
        # 实例状态
        self.status = status
        # 实例状态说明
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_provisioning_task_id is not None:
            result['LastProvisioningTaskId'] = self.last_provisioning_task_id
        if self.last_successful_provisioning_task_id is not None:
            result['LastSuccessfulProvisioningTaskId'] = self.last_successful_provisioning_task_id
        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_arn is not None:
            result['ProvisionedProductArn'] = self.provisioned_product_arn
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.provisioned_product_type is not None:
            result['ProvisionedProductType'] = self.provisioned_product_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastProvisioningTaskId') is not None:
            self.last_provisioning_task_id = m.get('LastProvisioningTaskId')
        if m.get('LastSuccessfulProvisioningTaskId') is not None:
            self.last_successful_provisioning_task_id = m.get('LastSuccessfulProvisioningTaskId')
        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductArn') is not None:
            self.provisioned_product_arn = m.get('ProvisionedProductArn')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('ProvisionedProductType') is not None:
            self.provisioned_product_type = m.get('ProvisionedProductType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class GetProvisionedProductResponseBody(TeaModel):
    def __init__(
        self,
        provisioned_product_detail: GetProvisionedProductResponseBodyProvisionedProductDetail = None,
        request_id: str = None,
    ):
        # 实例信息
        self.provisioned_product_detail = provisioned_product_detail
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.provisioned_product_detail:
            self.provisioned_product_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_detail is not None:
            result['ProvisionedProductDetail'] = self.provisioned_product_detail.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductDetail') is not None:
            temp_model = GetProvisionedProductResponseBodyProvisionedProductDetail()
            self.provisioned_product_detail = temp_model.from_map(m['ProvisionedProductDetail'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetProvisionedProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProvisionedProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResponseBodyTaskDetailLogTerraformLogs(TeaModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class GetTaskResponseBodyTaskDetailLog(TeaModel):
    def __init__(
        self,
        terraform_logs: List[GetTaskResponseBodyTaskDetailLogTerraformLogs] = None,
    ):
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = GetTaskResponseBodyTaskDetailLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class GetTaskResponseBodyTaskDetailOutputs(TeaModel):
    def __init__(
        self,
        description: str = None,
        output_key: str = None,
        output_value: str = None,
    ):
        self.description = description
        self.output_key = output_key
        self.output_value = output_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.output_value is not None:
            result['OutputValue'] = self.output_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        if m.get('OutputValue') is not None:
            self.output_value = m.get('OutputValue')
        return self


class GetTaskResponseBodyTaskDetailParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class GetTaskResponseBodyTaskDetail(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        log: GetTaskResponseBodyTaskDetailLog = None,
        outputs: List[GetTaskResponseBodyTaskDetailOutputs] = None,
        parameters: List[GetTaskResponseBodyTaskDetailParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        status: str = None,
        status_message: str = None,
        task_id: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        self.log = log
        self.outputs = outputs
        self.parameters = parameters
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 实例名称
        self.provisioned_product_name = provisioned_product_name
        # 任务状态
        self.status = status
        # 任务状态说明
        self.status_message = status_message
        # 任务ID
        self.task_id = task_id
        # 任务类型
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        if self.log:
            self.log.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Log') is not None:
            temp_model = GetTaskResponseBodyTaskDetailLog()
            self.log = temp_model.from_map(m['Log'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = GetTaskResponseBodyTaskDetailOutputs()
                self.outputs.append(temp_model.from_map(k))
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = GetTaskResponseBodyTaskDetailParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_detail: GetTaskResponseBodyTaskDetail = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 任务信息
        self.task_detail = task_detail

    def validate(self):
        if self.task_detail:
            self.task_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_detail is not None:
            result['TaskDetail'] = self.task_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskDetail') is not None:
            temp_model = GetTaskResponseBodyTaskDetail()
            self.task_detail = temp_model.from_map(m['TaskDetail'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
        product_version_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id
        # 产品版本ID
        self.product_version_id = product_version_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_body: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 模板内容
        self.template_body = template_body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_body is not None:
            result['TemplateBody'] = self.template_body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateBody') is not None:
            self.template_body = m.get('TemplateBody')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LaunchProductRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class LaunchProductRequest(TeaModel):
    def __init__(
        self,
        parameters: List[LaunchProductRequestParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_name: str = None,
        stack_region_id: str = None,
    ):
        self.parameters = parameters
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品版本ID
        self.product_version_id = product_version_id
        # 实例名称
        self.provisioned_product_name = provisioned_product_name
        # ROS资源栈所属的地域ID
        self.stack_region_id = stack_region_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = LaunchProductRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        return self


class LaunchProductResponseBody(TeaModel):
    def __init__(
        self,
        provisioned_product_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class LaunchProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: LaunchProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = LaunchProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConstraintsRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class ListConstraintsResponseBodyConstraintDetails(TeaModel):
    def __init__(
        self,
        config: str = None,
        constraint_id: str = None,
        constraint_type: str = None,
        create_time: str = None,
        description: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
    ):
        # 约束配置
        self.config = config
        # 约束ID
        self.constraint_id = constraint_id
        # 约束类型
        self.constraint_type = constraint_type
        # 创建时间
        self.create_time = create_time
        # 约束描述
        self.description = description
        # 约束所属的产品组合ID
        self.portfolio_id = portfolio_id
        # 约束对应的产品ID
        self.product_id = product_id
        self.product_name = product_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        return self


class ListConstraintsResponseBody(TeaModel):
    def __init__(
        self,
        constraint_details: List[ListConstraintsResponseBodyConstraintDetails] = None,
        request_id: str = None,
    ):
        # 约束详情
        self.constraint_details = constraint_details
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.constraint_details:
            for k in self.constraint_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstraintDetails'] = []
        if self.constraint_details is not None:
            for k in self.constraint_details:
                result['ConstraintDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constraint_details = []
        if m.get('ConstraintDetails') is not None:
            for k in m.get('ConstraintDetails'):
                temp_model = ListConstraintsResponseBodyConstraintDetails()
                self.constraint_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListConstraintsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListConstraintsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListConstraintsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListLaunchOptionsRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries(TeaModel):
    def __init__(
        self,
        constraint_type: str = None,
        description: str = None,
    ):
        # 约束类型
        self.constraint_type = constraint_type
        # 约束描述
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_type is not None:
            result['ConstraintType'] = self.constraint_type
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintType') is not None:
            self.constraint_type = m.get('ConstraintType')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class ListLaunchOptionsResponseBodyLaunchOptionSummaries(TeaModel):
    def __init__(
        self,
        constraint_summaries: List[ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries] = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
    ):
        # 约束概要
        self.constraint_summaries = constraint_summaries
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品组合名称
        self.portfolio_name = portfolio_name

    def validate(self):
        if self.constraint_summaries:
            for k in self.constraint_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConstraintSummaries'] = []
        if self.constraint_summaries is not None:
            for k in self.constraint_summaries:
                result['ConstraintSummaries'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.constraint_summaries = []
        if m.get('ConstraintSummaries') is not None:
            for k in m.get('ConstraintSummaries'):
                temp_model = ListLaunchOptionsResponseBodyLaunchOptionSummariesConstraintSummaries()
                self.constraint_summaries.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        return self


class ListLaunchOptionsResponseBody(TeaModel):
    def __init__(
        self,
        launch_option_summaries: List[ListLaunchOptionsResponseBodyLaunchOptionSummaries] = None,
        request_id: str = None,
    ):
        # 启动选项概要
        self.launch_option_summaries = launch_option_summaries
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.launch_option_summaries:
            for k in self.launch_option_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LaunchOptionSummaries'] = []
        if self.launch_option_summaries is not None:
            for k in self.launch_option_summaries:
                result['LaunchOptionSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_option_summaries = []
        if m.get('LaunchOptionSummaries') is not None:
            for k in m.get('LaunchOptionSummaries'):
                temp_model = ListLaunchOptionsResponseBodyLaunchOptionSummaries()
                self.launch_option_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListLaunchOptionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListLaunchOptionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListLaunchOptionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPortfoliosRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 过滤条件的名称
        self.key = key
        # 过滤条件的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListPortfoliosRequest(TeaModel):
    def __init__(
        self,
        filters: List[ListPortfoliosRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        scope: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # 过滤条件
        self.filters = filters
        self.page_number = page_number
        self.page_size = page_size
        # 产品ID
        self.product_id = product_id
        self.scope = scope
        # 排序字段
        self.sort_by = sort_by
        # 排序方式
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListPortfoliosRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListPortfoliosResponseBodyPortfolioDetails(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        portfolio_arn: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 产品组合描述
        self.description = description
        # 产品组合ARN
        self.portfolio_arn = portfolio_arn
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品组合名称
        self.portfolio_name = portfolio_name
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_arn is not None:
            result['PortfolioArn'] = self.portfolio_arn
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioArn') is not None:
            self.portfolio_arn = m.get('PortfolioArn')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListPortfoliosResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        portfolio_details: List[ListPortfoliosResponseBodyPortfolioDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 产品组合列表
        self.portfolio_details = portfolio_details
        # 请求ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.portfolio_details:
            for k in self.portfolio_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['PortfolioDetails'] = []
        if self.portfolio_details is not None:
            for k in self.portfolio_details:
                result['PortfolioDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.portfolio_details = []
        if m.get('PortfolioDetails') is not None:
            for k in m.get('PortfolioDetails'):
                temp_model = ListPortfoliosResponseBodyPortfolioDetails()
                self.portfolio_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPortfoliosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPortfoliosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPortfoliosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrincipalsRequest(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        return self


class ListPrincipalsResponseBodyPrincipals(TeaModel):
    def __init__(
        self,
        principal_id: str = None,
        principal_type: str = None,
    ):
        # RAM实体ID
        self.principal_id = principal_id
        # RAM实体类型
        self.principal_type = principal_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.principal_id is not None:
            result['PrincipalId'] = self.principal_id
        if self.principal_type is not None:
            result['PrincipalType'] = self.principal_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrincipalId') is not None:
            self.principal_id = m.get('PrincipalId')
        if m.get('PrincipalType') is not None:
            self.principal_type = m.get('PrincipalType')
        return self


class ListPrincipalsResponseBody(TeaModel):
    def __init__(
        self,
        principals: List[ListPrincipalsResponseBodyPrincipals] = None,
        request_id: str = None,
    ):
        # RAM实体列表
        self.principals = principals
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.principals:
            for k in self.principals:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Principals'] = []
        if self.principals is not None:
            for k in self.principals:
                result['Principals'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.principals = []
        if m.get('Principals') is not None:
            for k in m.get('Principals'):
                temp_model = ListPrincipalsResponseBodyPrincipals()
                self.principals.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPrincipalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrincipalsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPrincipalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductVersionsRequest(TeaModel):
    def __init__(
        self,
        product_id: str = None,
    ):
        # 产品版本所属的产品ID
        self.product_id = product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        return self


class ListProductVersionsResponseBodyProductVersionDetails(TeaModel):
    def __init__(
        self,
        active: bool = None,
        create_time: str = None,
        description: str = None,
        guidance: str = None,
        product_id: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        template_type: str = None,
        template_url: str = None,
    ):
        # 是否启用
        self.active = active
        # 创建时间
        self.create_time = create_time
        # 产品版本描述
        self.description = description
        # 推荐信息
        self.guidance = guidance
        self.product_id = product_id
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 模板类型
        self.template_type = template_type
        # 模板的OSS地址
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.template_type is not None:
            result['TemplateType'] = self.template_type
        if self.template_url is not None:
            result['TemplateUrl'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')
        if m.get('TemplateUrl') is not None:
            self.template_url = m.get('TemplateUrl')
        return self


class ListProductVersionsResponseBody(TeaModel):
    def __init__(
        self,
        product_version_details: List[ListProductVersionsResponseBodyProductVersionDetails] = None,
        request_id: str = None,
    ):
        # 产品版本列表
        self.product_version_details = product_version_details
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.product_version_details:
            for k in self.product_version_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ProductVersionDetails'] = []
        if self.product_version_details is not None:
            for k in self.product_version_details:
                result['ProductVersionDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.product_version_details = []
        if m.get('ProductVersionDetails') is not None:
            for k in m.get('ProductVersionDetails'):
                temp_model = ListProductVersionsResponseBodyProductVersionDetails()
                self.product_version_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListProductVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsAsAdminRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 过滤条件的名称
        self.key = key
        # 过滤条件的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductsAsAdminRequest(TeaModel):
    def __init__(
        self,
        filters: List[ListProductsAsAdminRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        portfolio_id: str = None,
        scope: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # 过滤条件
        self.filters = filters
        self.page_number = page_number
        self.page_size = page_size
        # 产品组合ID
        self.portfolio_id = portfolio_id
        self.scope = scope
        # 排序字段
        self.sort_by = sort_by
        # 排序方式
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProductsAsAdminRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductsAsAdminResponseBodyProductDetails(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
    ):
        # 产品创建时间
        self.create_time = create_time
        # 产品描述
        self.description = description
        # 产品ARN
        self.product_arn = product_arn
        # 产品ID
        self.product_id = product_id
        # 产品名字
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 产品提供方
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListProductsAsAdminResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_details: List[ListProductsAsAdminResponseBodyProductDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 产品列表
        self.product_details = product_details
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.product_details:
            for k in self.product_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProductDetails'] = []
        if self.product_details is not None:
            for k in self.product_details:
                result['ProductDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.product_details = []
        if m.get('ProductDetails') is not None:
            for k in m.get('ProductDetails'):
                temp_model = ListProductsAsAdminResponseBodyProductDetails()
                self.product_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsAsAdminResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsAsAdminResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsAsAdminResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsAsEndUserRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 过滤条件的名称
        self.key = key
        # 过滤条件的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProductsAsEndUserRequest(TeaModel):
    def __init__(
        self,
        filters: List[ListProductsAsEndUserRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # 过滤条件
        self.filters = filters
        self.page_number = page_number
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 排序方式
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProductsAsEndUserRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProductsAsEndUserResponseBodyProductSummaries(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        has_default_launch_option: bool = None,
        product_arn: str = None,
        product_id: str = None,
        product_name: str = None,
        product_type: str = None,
        provider_name: str = None,
    ):
        # 产品创建时间
        self.create_time = create_time
        # 产品描述
        self.description = description
        # 是否存在默认的启动选项
        self.has_default_launch_option = has_default_launch_option
        # 产品ARN
        self.product_arn = product_arn
        # 产品ID
        self.product_id = product_id
        # 产品名字
        self.product_name = product_name
        # 产品类型
        self.product_type = product_type
        # 产品提供方
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.has_default_launch_option is not None:
            result['HasDefaultLaunchOption'] = self.has_default_launch_option
        if self.product_arn is not None:
            result['ProductArn'] = self.product_arn
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HasDefaultLaunchOption') is not None:
            self.has_default_launch_option = m.get('HasDefaultLaunchOption')
        if m.get('ProductArn') is not None:
            self.product_arn = m.get('ProductArn')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class ListProductsAsEndUserResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        product_summaries: List[ListProductsAsEndUserResponseBodyProductSummaries] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 产品列表
        self.product_summaries = product_summaries
        # Id of the request
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.product_summaries:
            for k in self.product_summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProductSummaries'] = []
        if self.product_summaries is not None:
            for k in self.product_summaries:
                result['ProductSummaries'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.product_summaries = []
        if m.get('ProductSummaries') is not None:
            for k in m.get('ProductSummaries'):
                temp_model = ListProductsAsEndUserResponseBodyProductSummaries()
                self.product_summaries.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProductsAsEndUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsAsEndUserResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsAsEndUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProvisionedProductsRequestFilters(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 过滤条件的名称
        self.key = key
        # 过滤条件的值
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListProvisionedProductsRequest(TeaModel):
    def __init__(
        self,
        access_level_filter: str = None,
        filters: List[ListProvisionedProductsRequestFilters] = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # 访问过滤器
        self.access_level_filter = access_level_filter
        # 过滤条件
        self.filters = filters
        self.page_number = page_number
        self.page_size = page_size
        # 排序字段
        self.sort_by = sort_by
        # 排序方式
        self.sort_order = sort_order

    def validate(self):
        if self.filters:
            for k in self.filters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_level_filter is not None:
            result['AccessLevelFilter'] = self.access_level_filter
        result['Filters'] = []
        if self.filters is not None:
            for k in self.filters:
                result['Filters'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessLevelFilter') is not None:
            self.access_level_filter = m.get('AccessLevelFilter')
        self.filters = []
        if m.get('Filters') is not None:
            for k in m.get('Filters'):
                temp_model = ListProvisionedProductsRequestFilters()
                self.filters.append(temp_model.from_map(k))
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListProvisionedProductsResponseBodyProvisionedProductDetails(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        last_provisioning_task_id: str = None,
        last_successful_provisioning_task_id: str = None,
        last_task_id: str = None,
        owner_principal_id: str = None,
        owner_principal_type: str = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_arn: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        provisioned_product_type: str = None,
        stack_id: str = None,
        stack_region_id: str = None,
        status: str = None,
        status_message: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        # 上一次执行的实例操作任务ID
        self.last_provisioning_task_id = last_provisioning_task_id
        # 上一次成功执行的实例操作任务ID
        self.last_successful_provisioning_task_id = last_successful_provisioning_task_id
        # 上一次执行的任务ID
        self.last_task_id = last_task_id
        # 归属人的RAM实体ID
        self.owner_principal_id = owner_principal_id
        # 归属人的RAM实体类型
        self.owner_principal_type = owner_principal_type
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 实例ARN
        self.provisioned_product_arn = provisioned_product_arn
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 实例名称
        self.provisioned_product_name = provisioned_product_name
        self.provisioned_product_type = provisioned_product_type
        # ROS资源栈的ID
        self.stack_id = stack_id
        # ROS资源栈所属的地域ID
        self.stack_region_id = stack_region_id
        # 实例状态
        self.status = status
        # 实例状态说明
        self.status_message = status_message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.last_provisioning_task_id is not None:
            result['LastProvisioningTaskId'] = self.last_provisioning_task_id
        if self.last_successful_provisioning_task_id is not None:
            result['LastSuccessfulProvisioningTaskId'] = self.last_successful_provisioning_task_id
        if self.last_task_id is not None:
            result['LastTaskId'] = self.last_task_id
        if self.owner_principal_id is not None:
            result['OwnerPrincipalId'] = self.owner_principal_id
        if self.owner_principal_type is not None:
            result['OwnerPrincipalType'] = self.owner_principal_type
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_arn is not None:
            result['ProvisionedProductArn'] = self.provisioned_product_arn
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.provisioned_product_type is not None:
            result['ProvisionedProductType'] = self.provisioned_product_type
        if self.stack_id is not None:
            result['StackId'] = self.stack_id
        if self.stack_region_id is not None:
            result['StackRegionId'] = self.stack_region_id
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LastProvisioningTaskId') is not None:
            self.last_provisioning_task_id = m.get('LastProvisioningTaskId')
        if m.get('LastSuccessfulProvisioningTaskId') is not None:
            self.last_successful_provisioning_task_id = m.get('LastSuccessfulProvisioningTaskId')
        if m.get('LastTaskId') is not None:
            self.last_task_id = m.get('LastTaskId')
        if m.get('OwnerPrincipalId') is not None:
            self.owner_principal_id = m.get('OwnerPrincipalId')
        if m.get('OwnerPrincipalType') is not None:
            self.owner_principal_type = m.get('OwnerPrincipalType')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductArn') is not None:
            self.provisioned_product_arn = m.get('ProvisionedProductArn')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('ProvisionedProductType') is not None:
            self.provisioned_product_type = m.get('ProvisionedProductType')
        if m.get('StackId') is not None:
            self.stack_id = m.get('StackId')
        if m.get('StackRegionId') is not None:
            self.stack_region_id = m.get('StackRegionId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class ListProvisionedProductsResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        provisioned_product_details: List[ListProvisionedProductsResponseBodyProvisionedProductDetails] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 实例列表
        self.provisioned_product_details = provisioned_product_details
        # 请求ID
        self.request_id = request_id
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.provisioned_product_details:
            for k in self.provisioned_product_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['ProvisionedProductDetails'] = []
        if self.provisioned_product_details is not None:
            for k in self.provisioned_product_details:
                result['ProvisionedProductDetails'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.provisioned_product_details = []
        if m.get('ProvisionedProductDetails') is not None:
            for k in m.get('ProvisionedProductDetails'):
                temp_model = ListProvisionedProductsResponseBodyProvisionedProductDetails()
                self.provisioned_product_details.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListProvisionedProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProvisionedProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProvisionedProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        # 地域名称
        self.local_name = local_name
        # 地域接入地址
        self.region_endpoint = region_endpoint
        # 地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        regions: List[ListRegionsResponseBodyRegions] = None,
        request_id: str = None,
    ):
        # 地域列表
        self.regions = regions
        # 请求ID
        self.request_id = request_id

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        provisioned_product_id: str = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 排序字段
        self.sort_by = sort_by
        # 排序方式
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListTasksResponseBodyTaskDetailsLogTerraformLogs(TeaModel):
    def __init__(
        self,
        command: str = None,
        content: str = None,
        stream: str = None,
    ):
        self.command = command
        self.content = content
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command is not None:
            result['Command'] = self.command
        if self.content is not None:
            result['Content'] = self.content
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class ListTasksResponseBodyTaskDetailsLog(TeaModel):
    def __init__(
        self,
        terraform_logs: List[ListTasksResponseBodyTaskDetailsLogTerraformLogs] = None,
    ):
        self.terraform_logs = terraform_logs

    def validate(self):
        if self.terraform_logs:
            for k in self.terraform_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TerraformLogs'] = []
        if self.terraform_logs is not None:
            for k in self.terraform_logs:
                result['TerraformLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.terraform_logs = []
        if m.get('TerraformLogs') is not None:
            for k in m.get('TerraformLogs'):
                temp_model = ListTasksResponseBodyTaskDetailsLogTerraformLogs()
                self.terraform_logs.append(temp_model.from_map(k))
        return self


class ListTasksResponseBodyTaskDetailsOutputs(TeaModel):
    def __init__(
        self,
        description: str = None,
        output_key: str = None,
        output_value: str = None,
    ):
        self.description = description
        self.output_key = output_key
        self.output_value = output_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.output_value is not None:
            result['OutputValue'] = self.output_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('OutputKey') is not None:
            self.output_key = m.get('OutputKey')
        if m.get('OutputValue') is not None:
            self.output_value = m.get('OutputValue')
        return self


class ListTasksResponseBodyTaskDetailsParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class ListTasksResponseBodyTaskDetails(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        log: ListTasksResponseBodyTaskDetailsLog = None,
        outputs: List[ListTasksResponseBodyTaskDetailsOutputs] = None,
        parameters: List[ListTasksResponseBodyTaskDetailsParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_name: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
        provisioned_product_id: str = None,
        provisioned_product_name: str = None,
        status: str = None,
        status_message: str = None,
        task_id: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        # 创建时间
        self.create_time = create_time
        self.log = log
        self.outputs = outputs
        self.parameters = parameters
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 实例名称
        self.provisioned_product_name = provisioned_product_name
        # 实例状态
        self.status = status
        # 实例状态说明
        self.status_message = status_message
        # 实例名称
        self.task_id = task_id
        # 实例ARN
        self.task_type = task_type
        self.update_time = update_time

    def validate(self):
        if self.log:
            self.log.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.log is not None:
            result['Log'] = self.log.to_map()
        result['Outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['Outputs'].append(k.to_map() if k else None)
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.provisioned_product_name is not None:
            result['ProvisionedProductName'] = self.provisioned_product_name
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Log') is not None:
            temp_model = ListTasksResponseBodyTaskDetailsLog()
            self.log = temp_model.from_map(m['Log'])
        self.outputs = []
        if m.get('Outputs') is not None:
            for k in m.get('Outputs'):
                temp_model = ListTasksResponseBodyTaskDetailsOutputs()
                self.outputs.append(temp_model.from_map(k))
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = ListTasksResponseBodyTaskDetailsParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('ProvisionedProductName') is not None:
            self.provisioned_product_name = m.get('ProvisionedProductName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        task_details: List[ListTasksResponseBodyTaskDetails] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        # 请求ID
        self.request_id = request_id
        # 实例列表
        self.task_details = task_details
        # 总记录数
        self.total_count = total_count

    def validate(self):
        if self.task_details:
            for k in self.task_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TaskDetails'] = []
        if self.task_details is not None:
            for k in self.task_details:
                result['TaskDetails'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.task_details = []
        if m.get('TaskDetails') is not None:
            for k in m.get('TaskDetails'):
                temp_model = ListTasksResponseBodyTaskDetails()
                self.task_details.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TerminateProvisionedProductRequest(TeaModel):
    def __init__(
        self,
        provisioned_product_id: str = None,
    ):
        # 实例ID
        self.provisioned_product_id = provisioned_product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        return self


class TerminateProvisionedProductResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TerminateProvisionedProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TerminateProvisionedProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TerminateProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConstraintRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
        constraint_id: str = None,
        description: str = None,
    ):
        # 约束配置
        self.config = config
        # 约束ID
        self.constraint_id = constraint_id
        # 约束描述
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Config') is not None:
            self.config = m.get('Config')
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class UpdateConstraintResponseBody(TeaModel):
    def __init__(
        self,
        constraint_id: str = None,
        request_id: str = None,
    ):
        # 约束ID
        self.constraint_id = constraint_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.constraint_id is not None:
            result['ConstraintId'] = self.constraint_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConstraintId') is not None:
            self.constraint_id = m.get('ConstraintId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConstraintResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateConstraintResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateConstraintResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdatePortfolioRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        portfolio_id: str = None,
        portfolio_name: str = None,
        provider_name: str = None,
    ):
        # 产品组合描述
        self.description = description
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品组合名称
        self.portfolio_name = portfolio_name
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.portfolio_name is not None:
            result['PortfolioName'] = self.portfolio_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('PortfolioName') is not None:
            self.portfolio_name = m.get('PortfolioName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class UpdatePortfolioResponseBody(TeaModel):
    def __init__(
        self,
        portfolio_id: str = None,
        request_id: str = None,
    ):
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdatePortfolioResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdatePortfolioResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdatePortfolioResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        product_id: str = None,
        product_name: str = None,
        provider_name: str = None,
    ):
        # 产品描述
        self.description = description
        # 产品ID
        self.product_id = product_id
        # 产品名称
        self.product_name = product_name
        # 提供者名称
        self.provider_name = provider_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_name is not None:
            result['ProductName'] = self.product_name
        if self.provider_name is not None:
            result['ProviderName'] = self.provider_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductName') is not None:
            self.product_name = m.get('ProductName')
        if m.get('ProviderName') is not None:
            self.provider_name = m.get('ProviderName')
        return self


class UpdateProductResponseBody(TeaModel):
    def __init__(
        self,
        product_id: str = None,
        request_id: str = None,
    ):
        # 产品ID
        self.product_id = product_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProductVersionRequest(TeaModel):
    def __init__(
        self,
        active: bool = None,
        description: str = None,
        guidance: str = None,
        product_version_id: str = None,
        product_version_name: str = None,
    ):
        # 是否启用
        self.active = active
        # 产品版本描述
        self.description = description
        # 推荐信息
        self.guidance = guidance
        # 产品版本ID
        self.product_version_id = product_version_id
        # 产品版本名称
        self.product_version_name = product_version_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active is not None:
            result['Active'] = self.active
        if self.description is not None:
            result['Description'] = self.description
        if self.guidance is not None:
            result['Guidance'] = self.guidance
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.product_version_name is not None:
            result['ProductVersionName'] = self.product_version_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Active') is not None:
            self.active = m.get('Active')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Guidance') is not None:
            self.guidance = m.get('Guidance')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProductVersionName') is not None:
            self.product_version_name = m.get('ProductVersionName')
        return self


class UpdateProductVersionResponseBody(TeaModel):
    def __init__(
        self,
        product_version_id: str = None,
        request_id: str = None,
    ):
        # 产品版本ID
        self.product_version_id = product_version_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProductVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProductVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProductVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProvisionedProductRequestParameters(TeaModel):
    def __init__(
        self,
        parameter_key: str = None,
        parameter_value: str = None,
    ):
        self.parameter_key = parameter_key
        self.parameter_value = parameter_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parameter_key is not None:
            result['ParameterKey'] = self.parameter_key
        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterKey') is not None:
            self.parameter_key = m.get('ParameterKey')
        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')
        return self


class UpdateProvisionedProductRequest(TeaModel):
    def __init__(
        self,
        parameters: List[UpdateProvisionedProductRequestParameters] = None,
        portfolio_id: str = None,
        product_id: str = None,
        product_version_id: str = None,
        provisioned_product_id: str = None,
    ):
        self.parameters = parameters
        # 产品组合ID
        self.portfolio_id = portfolio_id
        # 产品ID
        self.product_id = product_id
        # 产品版本ID
        self.product_version_id = product_version_id
        # 实例ID
        self.provisioned_product_id = provisioned_product_id

    def validate(self):
        if self.parameters:
            for k in self.parameters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Parameters'] = []
        if self.parameters is not None:
            for k in self.parameters:
                result['Parameters'].append(k.to_map() if k else None)
        if self.portfolio_id is not None:
            result['PortfolioId'] = self.portfolio_id
        if self.product_id is not None:
            result['ProductId'] = self.product_id
        if self.product_version_id is not None:
            result['ProductVersionId'] = self.product_version_id
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.parameters = []
        if m.get('Parameters') is not None:
            for k in m.get('Parameters'):
                temp_model = UpdateProvisionedProductRequestParameters()
                self.parameters.append(temp_model.from_map(k))
        if m.get('PortfolioId') is not None:
            self.portfolio_id = m.get('PortfolioId')
        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')
        if m.get('ProductVersionId') is not None:
            self.product_version_id = m.get('ProductVersionId')
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        return self


class UpdateProvisionedProductResponseBody(TeaModel):
    def __init__(
        self,
        provisioned_product_id: str = None,
        request_id: str = None,
    ):
        # 实例ID
        self.provisioned_product_id = provisioned_product_id
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.provisioned_product_id is not None:
            result['ProvisionedProductId'] = self.provisioned_product_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProvisionedProductId') is not None:
            self.provisioned_product_id = m.get('ProvisionedProductId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateProvisionedProductResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProvisionedProductResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProvisionedProductResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


