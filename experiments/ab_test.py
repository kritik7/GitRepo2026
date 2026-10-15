"""Run a two-sided, pooled z-test for two conversion rates."""

from math import erf, sqrt


def compare_conversion_rates(
    control_visitors: int,
    control_conversions: int,
    variant_visitors: int,
    variant_conversions: int,
) -> tuple[float, float, float]:
    """Return (control rate, variant rate, two-sided p-value)."""
    if control_visitors <= 0 or variant_visitors <= 0:
        raise ValueError("Each group must have at least one visitor.")
    if not 0 <= control_conversions <= control_visitors:
        raise ValueError("Control conversions must be between zero and visitors.")
    if not 0 <= variant_conversions <= variant_visitors:
        raise ValueError("Variant conversions must be between zero and visitors.")

    control_rate = control_conversions / control_visitors
    variant_rate = variant_conversions / variant_visitors
    pooled_rate = (control_conversions + variant_conversions) / (
        control_visitors + variant_visitors
    )
    standard_error = sqrt(
        pooled_rate
        * (1 - pooled_rate)
        * (1 / control_visitors + 1 / variant_visitors)
    )

    if standard_error == 0:
        p_value = 1.0
    else:
        z_score = (variant_rate - control_rate) / standard_error
        p_value = 1 - erf(abs(z_score) / sqrt(2))

    return control_rate, variant_rate, p_value


def main() -> None:
    # Synthetic example only: 1,000 visitors in each randomly assigned group.
    control_visitors, control_conversions = 1_000, 120
    variant_visitors, variant_conversions = 1_000, 145
    control_rate, variant_rate, p_value = compare_conversion_rates(
        control_visitors,
        control_conversions,
        variant_visitors,
        variant_conversions,
    )

    difference = variant_rate - control_rate
    print(f"Control conversion rate: {control_rate:.2%}")
    print(f"Variant conversion rate: {variant_rate:.2%}")
    print(f"Absolute difference: {difference:+.2%}")
    print(f"Two-sided p-value: {p_value:.4f}")
    print(
        "Conclusion at alpha = 0.05: "
        + ("statistically significant" if p_value < 0.05 else "not statistically significant")
    )


if __name__ == "__main__":
    main()
