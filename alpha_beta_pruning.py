MAX_SCORE = 1000
MIN_SCORE = -1000


def minimax(depth, node_index, is_maximizing, values, alpha, beta):
    if depth == 3:
        return values[node_index]

    if is_maximizing:
        best_score = MIN_SCORE

        for i in range(2):
            score = minimax(depth + 1, node_index * 2 + i, False, values, alpha, beta)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)

            if beta <= alpha:
                break
        return best_score

    else:
        best_score = MAX_SCORE

        # Check both children (left and right)
        for i in range(2):
            score = minimax(depth + 1, node_index * 2 + i, True, values, alpha, beta)
            best_score = min(best_score, score)
            beta = min(beta, best_score)

            # Alpha-Beta Pruning: cut off search if beta <= alpha
            if beta <= alpha:
                break
        return best_score


# Driver Code
if __name__ == "__main__":
    leaf_values = [3, 5, 6, 9, 1, 2, 0, -1]

    optimal_value = minimax(
        depth=0,
        node_index=0,
        is_maximizing=True,
        values=leaf_values,
        alpha=MIN_SCORE,
        beta=MAX_SCORE
    )

    print("The optimal value is:", optimal_value)
