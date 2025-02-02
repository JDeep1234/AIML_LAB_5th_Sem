def minimax(t, ai_turn, a, b):
    if t >= 20:
        return -1 if ai_turn else 1 if t > 20 else 0

    best = -float('inf') if ai_turn else float('inf')
    
    for move in [1, 2, 3]:
        score = minimax(t + move, not ai_turn, a, b)
        
        if ai_turn:
            best = max(best, score)
            a = max(a, score)
        else:
            best = min(best, score)
            b = min(b, score)
        
        if b <= a:
            break
    return best

t = 0

while t < 20:
    player = int(input("Your move (1, 2, 3): "))
    while player not in [1, 2, 3]:
        player = int(input("Invalid. Enter 1, 2, or 3: "))
    t += player
    print(f"Total: {t}")
    
    if t >= 20:
        print("You win!")
        break

    print("AI's turn...")
    ai_move = max((minimax(t + m, False, -float('inf'), float('inf')), m) for m in [1, 2, 3])[1]
    t += ai_move
    print(f"AI picks {ai_move}. Total: {t}")
    
    if t >= 20:
        print("AI wins!")
        break
