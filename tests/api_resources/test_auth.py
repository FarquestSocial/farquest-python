# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from farquest import Farquest, AsyncFarquest

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAuth:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_callback(self, client: Farquest) -> None:
        auth = client.auth.callback(
            state="string",
        )
        assert auth is None

    @parametrize
    def test_raw_response_callback(self, client: Farquest) -> None:
        response = client.auth.with_raw_response.callback(
            state="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_callback(self, client: Farquest) -> None:
        with client.auth.with_streaming_response.callback(
            state="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_state(self, client: Farquest) -> None:
        auth = client.auth.retrieve_state(
            "string",
        )
        assert auth is None

    @parametrize
    def test_raw_response_retrieve_state(self, client: Farquest) -> None:
        response = client.auth.with_raw_response.retrieve_state(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = response.parse()
        assert auth is None

    @parametrize
    def test_streaming_response_retrieve_state(self, client: Farquest) -> None:
        with client.auth.with_streaming_response.retrieve_state(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_state(self, client: Farquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `state` but received ''"):
            client.auth.with_raw_response.retrieve_state(
                "",
            )


class TestAsyncAuth:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_callback(self, async_client: AsyncFarquest) -> None:
        auth = await async_client.auth.callback(
            state="string",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_callback(self, async_client: AsyncFarquest) -> None:
        response = await async_client.auth.with_raw_response.callback(
            state="string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_callback(self, async_client: AsyncFarquest) -> None:
        async with async_client.auth.with_streaming_response.callback(
            state="string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_state(self, async_client: AsyncFarquest) -> None:
        auth = await async_client.auth.retrieve_state(
            "string",
        )
        assert auth is None

    @parametrize
    async def test_raw_response_retrieve_state(self, async_client: AsyncFarquest) -> None:
        response = await async_client.auth.with_raw_response.retrieve_state(
            "string",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        auth = await response.parse()
        assert auth is None

    @parametrize
    async def test_streaming_response_retrieve_state(self, async_client: AsyncFarquest) -> None:
        async with async_client.auth.with_streaming_response.retrieve_state(
            "string",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            auth = await response.parse()
            assert auth is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_state(self, async_client: AsyncFarquest) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `state` but received ''"):
            await async_client.auth.with_raw_response.retrieve_state(
                "",
            )
