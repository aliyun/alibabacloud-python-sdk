# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddGatewayRouteShrinkRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        description: str = None,
        destination_type: str = None,
        direct_response_jsonshrink: str = None,
        domain_id: int = None,
        domain_id_list_json: str = None,
        enable_waf: bool = None,
        fallback: bool = None,
        fallback_services_shrink: str = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        name: str = None,
        policies: str = None,
        predicates_shrink: str = None,
        redirect_jsonshrink: str = None,
        route_order: int = None,
        route_type: str = None,
        services_shrink: str = None,
    ):
        # The language of the response. Valid values:
        # 
        # *   zh: Chinese
        # *   en: English
        self.accept_language = accept_language
        self.description = description
        # The type of the destination service. Valid values:
        # 
        # *   Single
        # *   Multiple
        # *   VersionOriented
        # *   Mock
        # *   Redirect
        self.destination_type = destination_type
        # The mock response configuration.
        self.direct_response_jsonshrink = direct_response_jsonshrink
        # The domain ID.
        self.domain_id = domain_id
        # The domain IDs.
        self.domain_id_list_json = domain_id_list_json
        # Specifies whether to activate Web Application Firewall (WAF).
        self.enable_waf = enable_waf
        # Specifies whether to enable the Fallback service.
        self.fallback = fallback
        # The information about the Fallback service.
        self.fallback_services_shrink = fallback_services_shrink
        # The ID of the gateway.
        self.gateway_id = gateway_id
        # The unique ID of the gateway.
        self.gateway_unique_id = gateway_unique_id
        # The name of the route.
        self.name = name
        # The routing policy in a JSON string.
        self.policies = policies
        # The matching rule.
        self.predicates_shrink = predicates_shrink
        # The configuration of the redirection.
        self.redirect_jsonshrink = redirect_jsonshrink
        # The sequence number of the route. (A small value indicates a high priority.)
        self.route_order = route_order
        # The route type. Valid values:
        # 
        # Op: Manage routes.
        self.route_type = route_type
        # The list of services.
        self.services_shrink = services_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.description is not None:
            result['Description'] = self.description

        if self.destination_type is not None:
            result['DestinationType'] = self.destination_type

        if self.direct_response_jsonshrink is not None:
            result['DirectResponseJSON'] = self.direct_response_jsonshrink

        if self.domain_id is not None:
            result['DomainId'] = self.domain_id

        if self.domain_id_list_json is not None:
            result['DomainIdListJSON'] = self.domain_id_list_json

        if self.enable_waf is not None:
            result['EnableWaf'] = self.enable_waf

        if self.fallback is not None:
            result['Fallback'] = self.fallback

        if self.fallback_services_shrink is not None:
            result['FallbackServices'] = self.fallback_services_shrink

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.name is not None:
            result['Name'] = self.name

        if self.policies is not None:
            result['Policies'] = self.policies

        if self.predicates_shrink is not None:
            result['Predicates'] = self.predicates_shrink

        if self.redirect_jsonshrink is not None:
            result['RedirectJSON'] = self.redirect_jsonshrink

        if self.route_order is not None:
            result['RouteOrder'] = self.route_order

        if self.route_type is not None:
            result['RouteType'] = self.route_type

        if self.services_shrink is not None:
            result['Services'] = self.services_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DestinationType') is not None:
            self.destination_type = m.get('DestinationType')

        if m.get('DirectResponseJSON') is not None:
            self.direct_response_jsonshrink = m.get('DirectResponseJSON')

        if m.get('DomainId') is not None:
            self.domain_id = m.get('DomainId')

        if m.get('DomainIdListJSON') is not None:
            self.domain_id_list_json = m.get('DomainIdListJSON')

        if m.get('EnableWaf') is not None:
            self.enable_waf = m.get('EnableWaf')

        if m.get('Fallback') is not None:
            self.fallback = m.get('Fallback')

        if m.get('FallbackServices') is not None:
            self.fallback_services_shrink = m.get('FallbackServices')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Policies') is not None:
            self.policies = m.get('Policies')

        if m.get('Predicates') is not None:
            self.predicates_shrink = m.get('Predicates')

        if m.get('RedirectJSON') is not None:
            self.redirect_jsonshrink = m.get('RedirectJSON')

        if m.get('RouteOrder') is not None:
            self.route_order = m.get('RouteOrder')

        if m.get('RouteType') is not None:
            self.route_type = m.get('RouteType')

        if m.get('Services') is not None:
            self.services_shrink = m.get('Services')

        return self

