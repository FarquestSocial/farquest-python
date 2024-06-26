# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import (
    make_request_options,
)

__all__ = ["ValidationResource", "AsyncValidationResource"]


class ValidationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ValidationResourceWithRawResponse:
        return ValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ValidationResourceWithStreamingResponse:
        return ValidationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get the validation criteria for a quest

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            f"/quest/validation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncValidationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncValidationResourceWithRawResponse:
        return AsyncValidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncValidationResourceWithStreamingResponse:
        return AsyncValidationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Get the validation criteria for a quest

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            f"/quest/validation/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class ValidationResourceWithRawResponse:
    def __init__(self, validation: ValidationResource) -> None:
        self._validation = validation

        self.retrieve = to_raw_response_wrapper(
            validation.retrieve,
        )


class AsyncValidationResourceWithRawResponse:
    def __init__(self, validation: AsyncValidationResource) -> None:
        self._validation = validation

        self.retrieve = async_to_raw_response_wrapper(
            validation.retrieve,
        )


class ValidationResourceWithStreamingResponse:
    def __init__(self, validation: ValidationResource) -> None:
        self._validation = validation

        self.retrieve = to_streamed_response_wrapper(
            validation.retrieve,
        )


class AsyncValidationResourceWithStreamingResponse:
    def __init__(self, validation: AsyncValidationResource) -> None:
        self._validation = validation

        self.retrieve = async_to_streamed_response_wrapper(
            validation.retrieve,
        )
